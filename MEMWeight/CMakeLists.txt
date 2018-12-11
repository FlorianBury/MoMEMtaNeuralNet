cmake_minimum_required(VERSION 3.2)

project(MEMWeight CXX)

# gflags package
add_subdirectory(external/gflags)

# Find MoMEMta
find_package(MoMEMta CONFIG REQUIRED)

find_package(ROOT 6.12 REQUIRED COMPONENTS TreePlayer)
find_library(ROOT_TREEPLAYER_LIBRARY TreePlayer HINTS ${ROOT_LIBRARY_DIR} REQUIRED)

# include matrix elements
add_subdirectory(MatrixElements/ME_TTbar)
add_subdirectory(MatrixElements/ME_DY)

# Flags necessary to ensure complex arithmetic performances on-par with
# Fortran code:
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-unused-variable -O3 -fcx-fortran-rules -fcx-limited-range -Wall -pedantic")
set(CMAKE_CXX_STANDARD 14)

include_directories(${ROOT_INCLUDE_DIR})

add_executable(
        MEMWeight
        "src/main.cc"
            )

# Set `confs` path
target_compile_definitions(MEMWeight PRIVATE CONFS_DIRECTORY="${CMAKE_SOURCE_DIR}/confs/")

target_link_libraries(MEMWeight Root::Root ${ROOT_TREEPLAYER_LIBRARY} momemta::momemta gflags)

