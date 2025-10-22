# ===========================
# ROS 2 Jazzy Dev Container
# ===========================

FROM ros:jazzy-ros-base-noble
# or ros:jazy-ros-base if you prefer minimal setup

# Ensure non-root user for development
ARG USERNAME=ubuntu

# Install basic development tools and GUI support
USER root

# Install basic development tools and GUI dependencies
RUN apt-get update && apt-get install -y \
    sudo \
    git \
    wget \
    vim \
    build-essential \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    x11-apps \
    clang-format \
    curl \
    pre-commit \
    nano \
    xvfb \
    x11vnc \
    netcat-traditional \
    ssh \
    apt-utils \
    net-tools \
    ros-jazzy-ros2-control \
    ros-jazzy-ros2-controllers \
    ros-jazzy-plotjuggler-ros \
    ros-jazzy-mavros \
    ros-jazzy-mavros-msgs \
    ros-jazzy-mavros-extras \
    gedit \
    python3-pip \
    python3-venv \
    python3-pandas

# Create a non-root user
RUN echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER $USERNAME
WORKDIR /home/$USERNAME

# Source ROS 2 setup in bashrc
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc

# Pre-create workspace structure
RUN mkdir -p /home/$USERNAME/colcon_ws/src

# Default command
CMD ["/bin/bash"]
