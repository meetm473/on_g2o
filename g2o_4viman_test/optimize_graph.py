#!/usr/bin/python3

import numpy as np
import g2o 
import os

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--max_iterations', type=int, default=5, help='perform n iterations')
parser.add_argument('-i', '--input', type=str, default='data/test.g2o', help='input file')
parser.add_argument('-o', '--output', type=str, default='data/test_opt.g2o', help='save resulting graph as file')
args = parser.parse_args()

dirName = os.path.dirname(__file__)

def main():
    solver = g2o.BlockSolverX(g2o.LinearSolverEigenX())
    solver = g2o.OptimizationAlgorithmLevenberg(solver)

    optimizer = g2o.SparseOptimizer()
    optimizer.set_verbose(True)
    optimizer.set_algorithm(solver)

    optimizer.load(os.path.join(dirName, args.input))
    print('num vertices:', len(optimizer.vertices()))
    print('num edges:', len(optimizer.edges()), end='\n\n')

    optimizer.initialize_optimization()
    optimizer.optimize(args.max_iterations)

    if len(args.output) > 0:
        optimizer.save(os.path.join(dirName, args.output))


if __name__ == '__main__':
    # assert os.path.isfile(args.input), (
    #     'Please provide a existing .g2o file')
        
    main()