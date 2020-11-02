include_directories(${CSPARSE_INCLUDE_DIR})

add_library(vm_slam_library SHARED 
			graph_types.h
			graph_types.cpp)


target_link_libraries(vm_slam_library 
					  ${G2O_LIBS})

add_executable(test_0
			   test_0.cpp)

target_link_libraries(test_0
					  vm_slam_library)
