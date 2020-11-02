cmake_minimum_required(VERSION 3.1)
project(on_g2o)

# Set output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/bin)

# Set header directory
set(HEADER_DIR ${PROJECT_SOURCE_DIR}/include ${G2O_INCLUDE_DIR})

# Set directory to search for G2O and other solvers
list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake_modules)

# Find G2O, Eigen3, CSparse packages
find_package(G2O)
if(G2O_FOUND)
	message(STATUS "Found G2O")
	SET(G2O_LIBS 
			g2o_cli
			g2o_ext_freeglut_minimal
			g2o_simulator
			g2o_solver_slam2d_linear
			g2o_types_icp
			g2o_types_slam2d
			g2o_core
			g2o_interface
			g2o_solver_csparse
			g2o_solver_structure_only
			g2o_types_sba
			g2o_types_slam3d
			g2o_csparse_extension
			g2o_opengl_helper
			g2o_solver_dense
			g2o_stuff
			g2o_types_sclam2d
			g2o_viewer
			g2o_parser
			g2o_solver_pcg
			g2o_types_data
			g2o_types_sim3 
			cxsparse
			)
else(G2O_FOUND)
	message(STATUS "Did not find G2O")
endif(G2O_FOUND)
find_package(CSparse)
find_package(Eigen3 3.3 REQUIRED)
if (TARGET Eigen3::Eigen)
  set(G2O_EIGEN3_EIGEN_TARGET Eigen3::Eigen)
else()
  include_directories(${EIGEN3_INCLUDE_DIR})
endif()

# Include directories
include_directories(${HEADER_DIR})

# Add sub-directories
add_subdirectory(tutorial_slam2d)