# slam_main

This project is for SLAM and Navigation in simulated environment about the ArduPilot SITL. Including some changes of the drone model,simulated environment, launch files, param configuration and some function added.


## Included packages

* `ardupilot_gz` - Contains simulating models controlled by ArduPilot SITL with DDS support in Gazebo.

* `ardupilot_ros` - Contains Cartographer and Nav2 function.

* `py_pubsub` - Contains pymavlink approach to control drone.

* `twist_to_twist_stamped` - Contains transform from /cmd_vel to different topic that needed.


## Prerequisites and Install

- Prerequisites can be found in ardupilot_gz and ardupilot_ros packages
- mavros related packages
- Octomap can generate the octreemap. Go to [OctoMap](https://github.com/OctoMap) and install Octomap, Octomap_server, Octomap_ros and Octomap_msgs if you want to use it. 
you can also install it in this way, but there may be some bugs that you cannot save the map(even though we haven't used it).
```bash
sudo apt install ros-<distro>-octomap-server
```

## Some commands to be useful

#### 1. Select simulated environment

```bash
ros2 launch ardupilot_gz_bringup iris_maze.launch.py rviz:=false
ros2 launch ardupilot_gz_bringup iris_warehouse.launch.py
```

#### 2. Launch Mavros or GCS
Mavros:
```bash
ros2 launch mavros apm.launch fcu_url:=udp://127.0.0.1:14550@14551
```
mavproxy:
```bash
mavproxy.py --console --map --aircraft test --master=:14551
```

#### 3. Cartographer

run the code:
```bash
ros2 launch ardupilot_ros cartographer.launch.py
```
save pbstream map:
```bash
ros2 service call /finish_trajectory cartographer_ros_msgs/srv/FinishTrajectory
ros2 service call /write_state cartographer_ros_msgs/srv/WriteState "{filename: '/home/ws2/ros2_ws/map3d.pbstream', include_unfinished_submaps: True}"
```
change to pgm file:
```bash
ros2 run cartographer_ros cartographer_pbstream_to_ros_map -map_filestem:/home/ws2/ros2_ws/rosmap -pbstream_filename=/home/ws2/ros2_ws/map.pbstream -resolution=0.05
```

#### 4. Octomap

run the code:
```bash
ros2 launch octomap_server octomap_mapping.launch.xml
```
save octree map:
```bash
ros2 run octomap_server octomap_saver_node --ros-args -p octomap_path:=(path for saving octomap) 
```
install and use octovis to see the map
```bash
octovis your_map.ot
```

#### 4. Nav2

Run related funtion in different control method:
Mavros(control velocity by pymavlink):
```bash
ros2 run py_pubsub pysetposition
```

mavproxy(control velocity by AP_DDS):
```bash
ros2 run twist_to_twist_stamped twist_to_twist_stamped
```

run the code:
```bash
ros2 launch ardupilot_ros navigation.launch.py
```
Note that the drone need to arm and take off before selecting the navigation point.

save pgm map:
```bash
ros2 run nav2_map_server map_saver_cli -f my_map
```

## Something can be configured

#### 1. Drone model
Go to /src/ardupilot_gz/ardupilot_gz_description/models/iris_with_lidar/model.sdf if you want to add new sensors to the drone such RGBD Camera or Imu sensor.

#### 2. Cartographer
Go to /src/ardupilot_ros/launch/cartographer.launch.py where you can select 2D or 3D SLAM and whether to load map.
Go to /src/ardupilot_ros/config where you can find .lua files, you can change the map generate parameter or sensors to SLAM(/points2 or /scan which means RGBD camera or laser) to get better result.
Now the 3D SLAM need the RGBD camera because laser is 2D laser which is not enough.

#### 3. Nav2
Go to /src/ardupilot_ros/config/navigation.yaml to change some navigate parameters such as robot_radius, inflation_radius, speed and the sensor to navigate(/points2 or /scan which means RGBD camera or laser).

