include_directories(${CSPARSE_INCLUDE_DIR})

add_library(tutorial_slam2d_library SHARED
  edge_se2_pointxy.cpp  se2.h   vertex_point_xy.h
  edge_se2.cpp    edge_se2_pointxy.h    vertex_se2.cpp
  edge_se2.h      vertex_point_xy.cpp  vertex_se2.h
  parameter_se2_offset.h parameter_se2_offset.cpp
  types_tutorial_slam2d.h types_tutorial_slam2d.cpp
  simulator.h simulator.cpp
  g2o_tutorial_slam2d_api.h
)

target_link_libraries(tutorial_slam2d_library ${G2O_LIBS})

add_executable(tutorial_slam2d
  tutorial_slam2d.cpp
)

target_link_libraries(tutorial_slam2d tutorial_slam2d_library)
