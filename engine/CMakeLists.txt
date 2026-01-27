# Binary EquaLab - C++ Math Engine
# Requirements: vcpkg with cln, ginac, eigen3, pybind11

cmake_minimum_required(VERSION 3.18)
project(equacore VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Find dependencies (via vcpkg)
find_package(PkgConfig REQUIRED)
pkg_check_modules(CLN REQUIRED cln)
pkg_check_modules(GINAC REQUIRED ginac)
find_package(Eigen3 3.4 REQUIRED NO_MODULE)
find_package(pybind11 CONFIG REQUIRED)

# Include directories
include_directories(
    ${CMAKE_SOURCE_DIR}/include
    ${CLN_INCLUDE_DIRS}
    ${GINAC_INCLUDE_DIRS}
)

# Core library (static)
add_library(equacore_static STATIC
    src/symbolic.cpp
    src/linear.cpp
)

target_link_libraries(equacore_static
    ${CLN_LIBRARIES}
    ${GINAC_LIBRARIES}
    Eigen3::Eigen
)

# Python bindings
pybind11_add_module(_equacore src/bindings.cpp)
target_link_libraries(_equacore PRIVATE equacore_static)

# Install Python module to python/equacore/
set_target_properties(_equacore PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/python/equacore
)

# Optional: WASM build (use -DBUILD_WASM=ON)
option(BUILD_WASM "Build WebAssembly module" OFF)
if(BUILD_WASM)
    message(STATUS "Building WASM module with Emscripten")
    set(CMAKE_EXECUTABLE_SUFFIX ".js")
    add_executable(equacore_wasm src/wasm_main.cpp)
    target_link_libraries(equacore_wasm equacore_static)
    set_target_properties(equacore_wasm PROPERTIES
        LINK_FLAGS "-s WASM=1 -s MODULARIZE=1 -s EXPORT_ES6=1"
        RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/wasm
    )
endif()
