# CMakeLists.txt for: culebra

set(BUILD_COMMAND ${PYTHON_EXECUTABLE} setup.py)
set(INSTALL_OPTIONS install -f --script-dir=${PROJ_BIN_DIR}) # These are for installation, not building. Ideally this would pass in from user some options.
install(CODE "execute_process(COMMAND ${BUILD_COMMAND} ${INSTALL_OPTIONS} WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/src/culebra)" RUNTIME DESTINATION bin)
# install(CODE "execute_process(COMMAND ${BUILD_COMMAND} install --install-lib ${OUTPUT_DIR}/lib WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})")'
# install(CODE "execute_process(COMMAND ${PYTHON_EXECUTABLE} setup.py install -f --prefix=${CMAKE_INSTALL_PREFIX} --script-dir=${PROJ_BIN_DIR} WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/src/culebra)"
#   RUNTIME DESTINATION bin)
