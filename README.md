# Mini Challenges Eq5
This repository contains the ROS2 packages for each of the mini challenges and final challenge developed for Manchester Robotics

## Final Challenge:
Each of the launch(s) or run(s) need to be in their own terminal.

### Launch/Run

#### Package Launch:
This launch excecutes the ML, Vision, Odometry and Controller nodes
```bash
cd github/mini_challenges_eq5

colcon build --packages-select final_challenge

source install/setup.bash

ros2 launch final_challenge final_launch.py
```

#### Camera Launch:
[ros_deep_learning repository](https://github.com/dusty-nv/ros_deep_learning)<br>
This launch excecutes the Jetson camera and sends video frames into the ```/video_source/raw``` topic
```bash
ros2 launch ros_deep_learning video_source.ros2.launch
```

#### Micro Ros Run:
[micro_ros repository](https://github.com/micro-ROS)<br>
This run excexutes micro ros for interfacing between the Jetson and Hackerboard
```bash
ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0
```

#### Foxglove Launch:
This launch establishes a connection to foxglove for topic visualization
```bash
ros2 launch foxglove_bridge foxglove_brige_launch.xml
```

### Topics
- ```/video_source/raw```: Original video frame 
- ```/cv_image```: Processed image for line follower
- ```/center_error```: Error in pixels for line follower (Line center - Center frame)
- ```/point_error```: Point error in pixels for line follower (Error between two points)
- ```/light```: Light detected
- ```/signal```: Signal detected
- ```/standby```: Boolean if an intersection is detected
- ```/VelocityEncL```: Left motor encoder
- ```/VelocityEncR```: Right motor encoder
- ```/odom```: Odometry of the robot
- ```/cmd_vel```: Linear and angular velocity of the robot
