# CMakeLists.txt for: culebra

#TODO: add an install option "SNAP", because most of the complexity here is for that. 
execute_process( COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/prepend_sitepackages.py $ENV{SNAPCRAFT_PART_INSTALL} mdkir
  OUTPUT_VARIABLE PYTHONPATH )

#install(CODE "execute_process(COMMAND PYTHONPATH=${PYTHONPATH})")
set(ENV{PYTHONPATH} $ENV{PYTHONPATH}:${PYTHONPATH})
set(PACKAGE_DIR ${CMAKE_SOURCE_DIR}/src/culebra)
set(PROJ_BIN_DIR "${CMAKE_SOURCE_DIR}/bin") # This should have been set three directories above but didn't seem to propagate
set(BUILD_COMMAND ${PYTHON_EXECUTABLE} setup.py develop) # trying pip and not setup to avoid pythonpath issues
set(DEVELOP_OPTIONS
  # --optimize=2

  --prefix=$ENV{SNAPCRAFT_PART_INSTALL}
  --build-directory=${CMAKE_SOURCE_DIR}/build
#  --install-dir=
#  --site-dirs 
#  --ignore-installed
   --script-dir=$ENV{SNAPCRAFT_PART_INSTALL}/bin # because cmake just 
  )
set(INSTALL_OPTIONS
  --force
  --optimize=2
  --build-directory=${CMAKE_SOURCE_DIR}/build
  --prefix=$ENV{SNAPCRAFT_PART_INSTALL}
  --install_scripts=${PROJ_BIN_DIR}
  )

message(STATUS "pypath     = $ENV{PYTHONPATH}")
message(STATUS "mypypath   = ${PYTHONPATH}")
message(STATUS "prefix     = $ENV{SNAPCRAFT_PART_INSTALL}")
message(STATUS "pkg dir    = ${PACKAGE_DIR}")
message(STATUS "projbindir = ${PROJ_BIN_DIR}")
message(STATUS "pyexe      = ${PYTHON_EXECUTABLE}")
message(STATUS "bld cmd    = ${BUILD_COMMAND}")
message(STATUS "instl opts = ${INSTALL_OPTIONS}")

install(CODE "execute_process(COMMAND ${BUILD_COMMAND} ${DEVELOP_OPTIONS} WORKING_DIRECTORY ${PACKAGE_DIR})")
# install(CODE "execute_process(COMMAND ${BUILD_COMMAND} install --install-lib ${OUTPUT_DIR}/lib WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})")'
# install(CODE "execute_process(COMMAND ${PYTHON_EXECUTABLE} setup.py install -f --prefix=${CMAKE_INSTALL_PREFIX} --script-dir=${PROJ_BIN_DIR} WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/src/culebra)"
#   RUNTIME DESTINATION bin)
