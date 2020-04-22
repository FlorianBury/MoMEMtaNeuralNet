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
add_subdirectory(MatrixElements/HToZA_1000_200)
add_subdirectory(MatrixElements/HToZA_1000_50)
add_subdirectory(MatrixElements/HToZA_1000_500)
add_subdirectory(MatrixElements/HToZA_2000_1000)
add_subdirectory(MatrixElements/HToZA_200_100)
add_subdirectory(MatrixElements/HToZA_200_50)
add_subdirectory(MatrixElements/HToZA_250_100)
add_subdirectory(MatrixElements/HToZA_250_50)
add_subdirectory(MatrixElements/HToZA_3000_2000)
add_subdirectory(MatrixElements/HToZA_300_100)
add_subdirectory(MatrixElements/HToZA_300_200)
add_subdirectory(MatrixElements/HToZA_300_50)
add_subdirectory(MatrixElements/HToZA_500_100)
add_subdirectory(MatrixElements/HToZA_500_200)
add_subdirectory(MatrixElements/HToZA_500_300)
add_subdirectory(MatrixElements/HToZA_500_400)
add_subdirectory(MatrixElements/HToZA_500_50)
add_subdirectory(MatrixElements/HToZA_650_50)
add_subdirectory(MatrixElements/HToZA_600_250)
add_subdirectory(MatrixElements/HToZA_800_100)
add_subdirectory(MatrixElements/HToZA_800_200)
add_subdirectory(MatrixElements/HToZA_800_400)
add_subdirectory(MatrixElements/HToZA_800_50)
add_subdirectory(MatrixElements/HToZA_800_700)


# Flags necessary to ensure complex arithmetic performances on-par with
# Fortran code:
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-unused-variable -O3 -fcx-fortran-rules -fcx-limited-range -Wall -pedantic")
set(CMAKE_CXX_STANDARD 14)

include_directories(${ROOT_INCLUDE_DIR})

add_executable(
        MEMWeight
        "src/main_TT.cc"
            )
#add_executable(
#        MEMWeight
#        "src/main_DY.cc"
#            )
#add_executable(
#        MEMWeight
#        "src/main_HToZA.cc"
#            )

# Set `confs` path
target_compile_definitions(MEMWeight PRIVATE CONFS_DIRECTORY="${CMAKE_SOURCE_DIR}/confs/")

target_link_libraries(MEMWeight Root::Root ${ROOT_TREEPLAYER_LIBRARY} momemta::momemta gflags)

