# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

cmake_minimum_required(VERSION 3.13)

project(SEALExamples VERSION 4.0.0 LANGUAGES CXX)

# Executable will be in bin
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)
set(SEAL_USE_CXX17 OFF)
set(CMAKE_BUILD_TYPE Release)

add_executable(keyGeneration keyGeneration.cpp)
add_executable(checkResult checkResult.cpp)

# In order to compute single-input function
add_executable(makeQuery makeQuery.cpp)
add_executable(makeQueryTwo makeQueryTwo.cpp)
add_executable(makeQueryThree makeQueryThree.cpp)

# Import Microsoft SEAL
find_package(SEAL 4.0.0 EXACT REQUIRED)

# Import OpenMP
find_package(OpenMP REQUIRED)
if(OpenMP_FOUND)
 set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
 set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()

# Link Microsoft SEAL
target_link_libraries(keyGeneration SEAL::seal)
target_link_libraries(checkResult SEAL::seal)

target_link_libraries(makeQuery SEAL::seal)
target_link_libraries(makeQueryTwo SEAL::seal)
target_link_libraries(makeQueryThree SEAL::seal)
