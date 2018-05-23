# CMakeLists.txt for: cmake_py
project(cmake_py)

#-----------------------------
# Python
FIND_PACKAGE(PythonInterp)
ADD_SUBDIRECTORY(culebra)

#-----------------------------
# C++
ADD_SUBDIRECTORY(veo)
