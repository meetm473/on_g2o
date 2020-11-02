#include "test_0.h"

int main(){
	
	

	// allocating optimizer
	SparseOptimizer optimizer;
	auto linearSolver = g2o::make_unique<SlamLinearSolver>();
	OptimizationAlgorithmGaussNewton* solver = new OptimizationAlgorithmGaussNewton(
				g2o::make_unique<SlamBlockSolver>(std::move(linearSolver)));

	optimizer.setAlgorithm(solver);

	// // add parameter representing the sensor offset
	// ParameterSE3Offset* sensorOffset = new ParameterSE3Offset;
	// sensorOffset->setOffset(sensorOffsetTransf);

	// add odometry to the optimizer
	// adding all vertices

	VertexSE3 r;
	// r.

	cout << "Optimization: Adding robot poses ... ";
	


	return 0;
}