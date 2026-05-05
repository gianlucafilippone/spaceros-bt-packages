FROM ros:humble-ros-base

WORKDIR /ros2_ws

COPY ./ros2_ws/src /ros2_ws/src

# Install dependencies and build
RUN apt update && apt install -y \
    python3-pip \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/* \
    && rosdep update

RUN apt-get update && rosdep install --from-paths src -y --ignore-src

RUN colcon build

ENTRYPOINT ["/bin/bash", "-c", "bash"]