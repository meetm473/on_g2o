#ifndef TEST_0_H
#define TEST_0_H

#include <iostream>
#include <cmath>

// Solvers and optimizers
#include <g2o/core/sparse_optimizer.h>
#include <g2o/core/block_solver.h>
#include <g2o/core/factory.h>
#include <g2o/core/optimization_algorithm_factory.h>
#include <g2o/core/optimization_algorithm_gauss_newton.h>
#include <g2o/solvers/csparse/linear_solver_csparse.h>

#include "graph_types.h"

using namespace std;
using namespace g2o;
using namespace g2o::viman;

typedef BlockSolver< BlockSolverTraits<-1, -1> >  SlamBlockSolver;
typedef LinearSolverCSparse<SlamBlockSolver::PoseMatrixType> SlamLinearSolver;

#endif