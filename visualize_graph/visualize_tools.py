#!/usr/bin/python3

import shlex
import string
import os

import matplotlib
import matplotlib.pyplot as plt
import math

dirName = os.path.dirname(__file__)

class slamData():
	"""
	SLAM data container for 2D.
	Reads G2O files and extracts data.

	Attributes
	---------
	landmarkX: array|Array of landmarks x position
	landmarkY: array|Array of landmarks y position 
	poseX: array|Array of poses x position
	poseY: array|Array of poses y position  
	poseA: array|Array of poses orentation (angle)

	Contructor parameters
	---------
	dataFilename: file name containing map in g2o format. (without .g2o)
	nodePose: keyword denoting pose
	nodeLandmark: keyword denoting landmark

	"""
	def __init__(self, dataFilename, _nodePose, _nodeLandmark):
		self.landmarkX = []
		self.landmarkY = []
		self.poseX = []
		self.poseY = []
		self.poseA = []
		self.nodeLandmark = _nodeLandmark
		self.nodePose = _nodePose
		self.getDataFromFile(dataFilename)

	def getDataFromFile(self, dataFilename):
		"""
		Fills object arrays with SLAM data given by file
			
		Parameters
		----------
		dataFilename: string
		filename with SLAM data in g2o format
		"""
		f = open(os.path.join(dirName, dataFilename), 'r')
		# get data loop
		for line in f:
		# split string
			lineWords = shlex.split(line)
			if str.find(lineWords[0], self.nodePose) != -1:
				# get robot pose
				self.poseX.append(float(lineWords[2]))
				self.poseY.append(float(lineWords[3]))
				self.poseA.append(float(lineWords[4]))
			elif str.find(lineWords[0], self.nodeLandmark) != -1:
				# get landmark position
				self.landmarkX.append(float(lineWords[2]))
				self.landmarkY.append(float(lineWords[3]))
		f.close()

def plotResults(filename, figFilename, showFig = False):	
	lw = 2
	ms = 8

	# get variables from file
	gtData = slamData(filename, "VERTEX_SE2", "VERTEX_XY")

	_,ax = plt.subplots()
	rbt_path, = ax.plot(gtData.poseX, gtData.poseY, '.-', color = '#bbbbf9', linewidth = lw, markersize = ms, label='robot path')
	land_path, = ax.plot(gtData.landmarkX, gtData.landmarkY, '.', color = '#800000', linewidth = lw, markersize = ms, label='landmarks')
	plt.grid(True)
	plt.legend(handles=[rbt_path,land_path])
	if showFig:
		plt.show()
	
	# print figure
	plt.savefig(os.path.join(dirName,"res",figFilename) + ".png", bbox_inches='tight')
	print("Saved the figure as: "+os.path.join(dirName,"res",figFilename) + ".png")