# robot_learning_ws
Code for the exercises in CS 309 Robot Learning (FRI I). 

### Note: these exercises require a machine with ROS Noetic and Ubuntu 20.04. See below for installation instructions. Do not attempt to run ROS in a VM. Dual boot if you wish (consult with a peer mentor and back up your data) or use the basement computer lab. 

## If you already have ROS installed: 
1. Set up your github ssh key. See the course website [here](https://www.cs.utexas.edu/~abba/fri-robot-learning/install_use_github.html). (You likely already have git and just need to add an ssh key). 
2. Clone this repo in your home directory like so:
```
cd
git clone git@github.com:UT-Austin-RobIn/robot_learning_ws.git
cd robot_learning_ws
git submodule init
git submodule update
```
3. Build the workspace
```
source /opt/ros/noetic/setup.bash
cd ~/robot_learning_ws
catkin_make
```
4. Run `source devel/setup.bash` so ROS can find packages in this workspace.
5. Run code for the exercises! 


## ROS installation instructions
1. Let's install ROS Noetic and the dependencies for the Sawyer robot. Make sure you have Ubuntu 20.04. If not, see [here](https://releases.ubuntu.com/focal/).
2. Setup sources and keys, then update
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt-get update
```
3. Install ROS
```
sudo apt-get install ros-noetic-desktop-full
```
4. Install Sawyer dependences
```
sudo apt-get install git-core python3-wstool python3-vcstools python3-rosdep ros-noetic-control-msgs ros-noetic-xacro ros-noetic-tf2-ros ros-noetic-rviz ros-noetic-cv-bridge ros-noetic-actionlib ros-noetic-actionlib-msgs ros-noetic-dynamic-reconfigure ros-noetic-trajectory-msgs ros-noetic-rospy-message-converter
sudo apt-get install ros-noetic-moveit
sudo apt-get install ros-noetic-rviz-visual-tools ros-noetic-moveit-visual-tools  
```
5. Initialize rosdep
```
sudo rosdep init
rosdep update
```
6. Proceeed with the instructions above to set up this repository.



