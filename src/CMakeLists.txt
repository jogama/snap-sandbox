# CMakeLists.txt for: cmake_py
project(cmake_py)

#-----------------------------
# Python
FIND_PACKAGE(PythonInterp)

#-----------------------------
# C++
ADD_SUBDIRECTORY(veo)
