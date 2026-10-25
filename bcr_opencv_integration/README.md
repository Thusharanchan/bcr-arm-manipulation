# ROS 2 Robotic Arm Motion Planning & Control (bcr_arm)

A ROS 2 simulation package configured for robotic arm motion planning, joint state control, and automated manipulation workflows.

## 🛠️ Tech Stack & Tools
* **Robotics Framework:** ROS 2 (Humble)
* **Simulation & Motion Planning:** Gazebo, MoveIt2, RViz2
* **Programming Language:** Python / C++

---

## 📌 Project Overview
This project utilizes the open-source `bcr_arm` simulation framework to implement kinematic control, trajectory planning, and pick-and-place behaviors in a virtual environment.

---

## 🚀 How to Build and Run

1. Clone this repository into the `src` directory of your ROS 2 workspace:
   ```bash
   cd ~/ros2_ws/src
   git clone [https://github.com/your-username/bcr-arm-manipulation.git]git clone https://github.com/ThusharAnchan/bcr-arm-manipulation.git

Build the workspace:
cd ~/ros2_ws
colcon build --packages-select bcr_arm

Source your environment and launch the arm simulation:
source install/setup.bash
ros2 launch bcr_arm arm_gazebo.launch.py
