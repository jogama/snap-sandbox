# CMakeLists.txt for: cmake_py
project(cmake_py)

#-----------------------------
# Python
FIND_PACKAGE(PythonInterp 3)
ADD_SUBDIRECTORY(culebra)

#-----------------------------
# C++
ADD_SUBDIRECTORY(veo)
