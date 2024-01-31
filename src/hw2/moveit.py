#! /usr/bin/env python
import rospy
import sys
import rospy
import moveit_commander
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from std_msgs.msg import Header
import tf2_ros
import tf2_geometry_msgs

import numpy as np 

WORLD_FRAME = "base"
EE_FRAME = "right_gripper_tip"
GROUP_NAME = "right_arm"

class RightArm(object):
    def __init__(self):
        super(RightArm, self).__init__()

        # initialize moveit 
        moveit_commander.roscpp_initialize(sys.argv)
        self.group = moveit_commander.MoveGroupCommander(GROUP_NAME)

        # Setup a transform buffer to swap poses between frames
        self.tf_buffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tf_buffer)

    def translate_in_ee_frame(self, distance):
        """
        Move the end-effector by @distance in the local frame of the end-effector. 
        @distance: np.array shape (3,)
        """
        
        # TODO: Create a PoseStamped message, @distance w.r.t the EE_FRAME
        # hint: use the following message types:
        # - Header(frame_id = ?)
        # - Point(x, y, z)
        # - Quaternion(x, y, z, w)
        # - Pose(position, rotation)
        # - PoseStamped(header, pose)

        # TODO: Transform the pose to WORLD_FRAME
        # hint: use self.tf_buffer.transform

        # TODO: Set the pose as target and go
        # hint: use self.group: self.group.set_pose_target and self.group.go 
        return

if __name__ == '__main__':

    # initialize node
    rospy.init_node('hw2_moveit')

    # create RightArm object
    arm = RightArm()

    # TODO: form a vector representing 5cm in the x-direction
    # this should be a numpy array of shape (3,)
    # displacement = ...

    arm.translate_in_ee_frame(displacement)