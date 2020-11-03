#!/usr/bin/python3

from visualize_tools import plot2
from slam_tools import slamData2D, optimizeGraph

def main():
	inputFile = "data/gtPath.g2o"
	outputFile = "data/gtPath_opt.g2o"

	optimizeGraph(inputFile,outputFile,10)

	print("Optimization finished")

	gData = slamData2D(outputFile,"VERTEX_SE2","VERTEX_XY")
	plot2(gData,"gtPath_opt")

if __name__ == "__main__":
	main()