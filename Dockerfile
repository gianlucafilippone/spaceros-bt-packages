FROM ros:humble-ros-base

WORKDIR /ros2_ws

COPY ./ros2_ws/src /ros2_ws/src

ENTRYPOINT ["/bin/bash", "-c", "bash"]