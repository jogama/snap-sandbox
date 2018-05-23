install(CODE "execute_process(COMMAND PYTHON_EXECUTABLE setup.py install -f
--prefix=${CMAKE_INSTALL_PREFIX} --script-dir=${PROJ_BIN_DIR} WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/src/culebra)")
