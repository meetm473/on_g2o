#!/usr/bin/python3

# import msvcrt 		# uncomment this for windows
import getch			# uncomment this for linux
import os

import numpy as np
import matplotlib.pyplot as plt
from spatialmath import base as tr

# VARS TO CUSTOMIZE
edge_se2_info_matrixG = " 1 0 0 1 0 1\r\n" # ipxx ipxy ipxa ipyy ipya ipaa (ideal)
transl_incre = 0.1		# units
rot_incre = 10			# deg
outputDir = "data"		# relative path (wrt dir this file's location)
gtFilename = "gtPath"
sensorFilename = "sensorPath"

""" DO NOT MODIFY """
# Transformation matrix: local to global
T = np.eye(3)

edge_se2_info_matrixS = " 1 0 0 1 0 1\r\n" # ipxx ipxy ipxa ipyy ipya ipaa (sensor)

heading = 0				# to store the current heading wrt global frame
pose_counter = 0		# to ID the pose

# for visualising ground truth motion
plt.ion()
fig, ax = plt.subplots()
plot = ax.scatter([],[])
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# vars to store final output
dirName = os.path.dirname(__file__)
f_gt = open(os.path.join(dirName, outputDir, gtFilename)+".g2o","w+")
f_sense = open(os.path.join(dirName, outputDir, sensorFilename)+".g2o","w+")

def help():
	"""
	Displays keyboard instructions that are accepted by the simulator.

	"""
	print('\n----\nInstructions:')
	print('Initially, robot faces positive x axis')
	print('w: moves forward by ', transl_incre)
	print('s: moves backward by ', transl_incre)
	print('a: rotates ccw by ', rot_incre, ' deg')
	print('d: rotates cw by ', rot_incre, 'deg')
	print('t: show current transformation matrix')
	print('q: quit and generate gtData.g2o, gtData.png, and sensorData.g2o files')
	print('h: display thelp')

def update_plot():
	"""
	Updates the figure showcasing live ground truth.
	"""
	global fig, ax, plot, T

	# get the current points as numpy array with shape  (N, 2)
	array = plot.get_offsets()

	# add the point to the plot
	array = np.concatenate([array, np.array([T[0][2], T[1][2]],ndmin=2)])

	plot.set_offsets(array)
	fig.canvas.draw()
	
	# update x and ylim to show all points:
	ax.set_xlim(array[:, 0].min() - 1, array[:,0].max() + 1)
	ax.set_ylim(array[:, 1].min() - 1, array[:, 1].max() + 1)

	plt.pause(0.01)

def sample_pose(trans_state, rot_state):
	"""
	Updates ./outputDir/gtFilename.g2o and ./outputDir/sensorFilename.g2o 
	rot_state = 0 -> Pure translation
			  = 1 -> ccw
			  = -1 -> cw 
	trans_state = 1 -> fwd
				= -1 -> bck
	"""
	global rot_incre, transl_incre
	global edge_se2_info_matrixG, pose_counter

	if rot_state:
		r = np.radians(rot_state*rot_incre)
		f_gt.write("EDGE_SE2 "+ str(pose_counter) + " " + str(pose_counter+1) + " 0 0 " + str(r) + edge_se2_info_matrixG)
	else:
		t = trans_state*transl_incre
		f_gt.write("EDGE_SE2 "+ str(pose_counter) + " " + str(pose_counter+1) + " "+ str(t) + " 0 0" + edge_se2_info_matrixG)
	pose_counter = pose_counter + 1

def file_setup():
	global f_gt, f_sense

	f_gt.write("VERTEX_SE2 0 0 0 0\r\n")
	f_gt.write("FIX 0\r\n")

	f_sense.write("VERTEX_SE2 0 0 0 0\r\n")
	f_sense.write("FIX 0\r\n")

def main():
	global T, fig, heading
	global f_gt, f_sense

	print('Welcome to 2D robot simulator')
	help()

	file_setup()

	while True:
		# ch = msvcrt.getwch() 			# uncomment this for windows
		ch = getch.getch() 				# uncomment this for linux
		if ch =='q':
			fig.savefig(os.path.join(dirName, outputDir, gtFilename+".png"))
			print('ground truth path saved as: ', os.path.join(dirName, outputDir), "/"+gtFilename+".png")
			f_sense.close()
			f_gt.close()
			print('ground truth path saved as: ', os.path.join(dirName,outputDir), "/"+gtFilename+".g2o")
			print('sensor path saved as: ', os.path.join(dirName,outputDir), "/"+sensorFilename+".g2o")
			break
		elif ch == 'h':
			help()
		elif ch == 'w':
			T = T @ tr.transl2(transl_incre,0)
			update_plot()
			sample_pose(1,0)
			print('moved forward')
		elif ch == 's':
			T = T @ tr.transl2(-transl_incre,0)
			update_plot()
			sample_pose(-1,0)
			print('moved backward')
		elif ch == 'a':
			T = T @ tr.trot2(rot_incre,'deg')
			heading = heading + rot_incre
			sample_pose(0,1)
			print('moved ccw | heading: ', heading)
		elif ch == 'd':
			T = T @ tr.trot2(-rot_incre,'deg')
			heading = heading - rot_incre
			sample_pose(0,-1)
			print('moved cw | heading: ', heading)
		elif ch == 't':
			print(T)

if __name__ == "__main__":
	main()