# UR5 Drone World Simulation Project

## Overview
![demo](UR5DEMO.gif)
This project contains the code and simulation world used to control a **Universal Robots UR5 robotic arm** inside a **custom Gazebo drone race track world**, using **ROS 2 Jazzy** and **Gazebo Harmonic**.

The system demonstrates:

- Loading a complex Gazebo world (drone race track with shifted gates)
- Spawning a UR5 robot using the official UR simulation packages
- Bridging ROS 2 ↔ Gazebo
- Controlling the UR5 with a custom **Python (rclpy)** node that sends joint trajectories (back-and-forth motion).

---

## Repository Structure

```text
UR5_DroneWorld_Project/
├─ code/
│  └─ ur_back_and_forth/
│     ├─ ur_back_and_forth.py      # Main Python ROS 2 node (back & forth motion)
│     └─ (optional) ur_rotate_demo.py  # Example: single big rotation demo
│
├─ gazebo_world/
│  └─ drone_race_track_2018_actual_with_gatepapers_shifted.world
│     # Custom world: drone race track with gates shifted
│
├─ video/
│  └─ ...                          # Demonstration videos
│
├─ presentation/
│  └─ ...                          # Internship / project presentation slides
│
├─ documents/
│  └─ ...                          # Reports and notes
│
└─ README.md                       # This file
