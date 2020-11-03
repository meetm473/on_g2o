#!/usr/bin/python3

import os

import matplotlib
import matplotlib.pyplot as plt

dirName = os.path.dirname(__file__)

def plot2(gData, figFilename, showFig = False):
	"""
	For plotting 2D SLAM

	Parameters:
	gData: graph data object of slamData2D type
	figFilename: name of image file to save the plot
	showFig: True | False (default)
	"""
	lw = 2
	ms = 8

	# get variables from file
	# gData = slamData(filename, "VERTEX_SE2", "VERTEX_XY")

	_,ax = plt.subplots()
	rbt_path, = ax.plot(gData.poseX, gData.poseY, '.-', color = '#0b03fc', linewidth = lw, markersize = ms, label='robot path')
	land_path, = ax.plot(gData.landmarkX, gData.landmarkY, '.', color = '#800000', linewidth = lw, markersize = ms, label='landmarks')
	plt.grid(True)
	plt.legend(handles=[rbt_path,land_path])
	if showFig:
		plt.show()
	
	# print figure
	plt.savefig(os.path.join(dirName,"res",figFilename) + ".png", bbox_inches='tight')
	print("Saved the figure as: "+os.path.join(dirName,"res",figFilename) + ".png")