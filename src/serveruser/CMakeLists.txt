# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

cmake_minimum_required(VERSION 3.13)

project(SEALExamples VERSION 4.0.0 LANGUAGES CXX)

# Executable will be in bin
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)
set(SEAL_USE_CXX17 OFF)
set(CMAKE_BUILD_TYPE Release)

add_executable(makeInput makeInput.cpp)
add_executable(makeInputTwo makeInputTwo.cpp)
add_executable(makeInputThree makeInputThree.cpp)

add_executable(searchInputTwo searchInputTwo.cpp)
# add_executable(extractOutputTwo extractOutputTwo.cpp)

add_executable(searchInputThree searchInputThree.cpp)
# add_executable(extractOutputThree extractOutputThree.cpp)

add_executable(searchInput searchInput.cpp)
# add_executable(extractOutput extractOutput.cpp)



# Import Microsoft SEAL
find_package(SEAL 4.0.0 EXACT REQUIRED)

# Import OpenMP
find_package(OpenMP REQUIRED)
if(OpenMP_FOUND)
 set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
 set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

# Link Microsoft SEAL
target_link_libraries(makeInputTwo SEAL::seal)
target_link_libraries(makeInputThree SEAL::seal)
target_link_libraries(makeInput SEAL::seal)

target_link_libraries(searchInputTwo SEAL::seal)
# target_link_libraries(extractOutputTwo SEAL::seal)

target_link_libraries(searchInputThree SEAL::seal)
# target_link_libraries(extractOutputThree SEAL::seal)

target_link_libraries(searchInput SEAL::seal)
# target_link_libraries(extractOutput SEAL::seal)
