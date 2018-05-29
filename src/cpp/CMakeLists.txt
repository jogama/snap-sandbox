# CMakeLists.txt for: veo

set(SRC
  caller.cpp)

add_executable(roll_call ${SRC})

install(TARGETS roll_call
  RUNTIME DESTINATION bin
  )
