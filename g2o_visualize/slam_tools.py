#!/usr/bin/python3

import os
import shlex

import numpy as np
import g2o

dirName = os.path.dirname(__file__)

class slamData2D():
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
	dataFilename: file name containing map in g2o format. (with .g2o)
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

def optimizeGraph(inputFile, outputFile, maxIterations):
	"""
	Optimizes the input graph
	"""
	solver = g2o.BlockSolverX(g2o.LinearSolverEigenX())
	solver = g2o.OptimizationAlgorithmLevenberg(solver)

	optimizer = g2o.SparseOptimizer()
	optimizer.set_verbose(True)
	optimizer.set_algorithm(solver)

	optimizer.load(os.path.join(dirName, inputFile))
	print('num vertices:', len(optimizer.vertices()))
	print('num edges:', len(optimizer.edges()), end='\n\n')

	optimizer.initialize_optimization()
	optimizer.optimize(maxIterations)

	optimizer.save(os.path.join(dirName, outputFile))