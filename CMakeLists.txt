cmake_minimum_required(VERSION 3.1)
project(on_g2o)

# Set output directories
set(RUNTIME_OUTPUT_DIR ${PROJECT_SOURCE_DIR}/bin)
set(LIB_OUTPUT_DIR ${PROJECT_SOURCE_DIR}/lib)

# Set header directory
set(HEADER_DIR ${PROJECT_SOURCE_DIR}/include)

# Set directory to search for G2O and other solvers
list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake_modules)

# Find G2O, Eigen3, CSparse packages
find_package(G2O)
if(G2O_FOUND)
	message(STATUS "Found G2O")
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