cmake_minimum_required(VERSION 3.5)
project(lunabot_simulation)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch models urdf worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

