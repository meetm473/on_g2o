cmake_minimum_required(VERSION 3.1)
project(on_g20)

include_directories(include)
link_directories(${PROJECT_SOURCE_DIR}/lib)

set(SOURCES src/a_curve_fit.cpp)

add_executable(a_curve_fit ${SOURCES})
target_link_libraries(a_curve_fit libg2o_core.so libg2o_stuff.so)

install(TARGETS a_curve_fit DESTINATION ${PROJECT_SOURCE_DIR}/bin)
