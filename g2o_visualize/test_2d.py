#!/usr/bin/python3

from visualize_tools import plot2
from slam_tools import slamData2D, optimizeGraph

def main():
	dirName = "data/"
	inputFile = "sensorPath"
	# inputFile = "gtPath"

	optimizeGraph(dirName+inputFile+".g2o",dirName+inputFile+"_opt.g2o",10)

	print("Optimization finished")

	gData = slamData2D(dirName+inputFile+"_opt.g2o","VERTEX_SE2","VERTEX_XY")
	plot2(gData, inputFile+"_opt")

if __name__ == "__main__":
	main()