cmake_minimum_required(VERSION 3.0)

project(NERD LANGUAGES C CXX)


# A log function to display files path in a list of files
function(MESSAGE_LIST_FILES FILES)
    foreach(FILE ${FILES})
        message("\t ${FILE}")
    endforeach()
endfunction()


# Environment
set(CMAKE_CXX_STANDARD 17)

# Building
message("cmake version : ${CMAKE_VERSION}")
message("\n\nStart building project ${PROJECT_NAME} ... \n")

# Check sources and headers
file(GLOB_RECURSE SRC_FILES src/*.c*)
message("Sources files founded : ")
MESSAGE_LIST_FILES("${SRC_FILES}")

file(GLOB_RECURSE INC_FILES include/*h*)
message("Includes files founded : ")
MESSAGE_LIST_FILES("${INC_FILES}")


# Platform setup
if (WIN32)
    message("\nPlatform context : WIN32")
    add_definitions(-D_WIN32)
    set(PLATFORM_SRC "src/platform_windows.c")
endif()
if (UNIX)
    message("\nPlatform context : UNIX")
    add_definitions(-D__linux__)
    set(PLATFORM_SRC "src/platform_linux.c")
endif()

# Generate executables
include_directories("include/")

add_executable(${PROJECT_NAME} "src/main.c" "src/features.cpp" "${PLATFORM_SRC}")
add_executable("${PROJECT_NAME}-test" "src/test.cpp" "src/features.cpp" "${PLATFORM_SRC}")

# Should be good to also have -Werror (warnings become errors)
target_compile_options(${PROJECT_NAME} PRIVATE -Wall -O2 -Wextra -ansi -pedantic) 

message("\nProject ${PROJECT_NAME} builded.\n")
