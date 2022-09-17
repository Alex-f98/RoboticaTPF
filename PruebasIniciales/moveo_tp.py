#! /usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi

if __name__ == '__main__':
    try:
        print("")
        print("----------------------------------------------------------")
        print("Bienvenido al simulador con Rviz en python")
        print("----------------------------------------------------------")
        print("Presiona Ctrl + D para salir")
        print("")

        input(
            "============ Press `Enter` para empezar"
        )
        #TP_integrador()
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('move_group_python_TP', anonymous=True)
        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        group_name = "arm"
        group = moveit_commander.MoveGroupCommander(group_name)
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
        moveit_msgs.msg.DisplayTrajectory)

        # We can get the joint values from the group and adjust some of the values:
        joint_goal = group.get_current_joint_values()
        joint_goal[0] = 0
        joint_goal[1] = pi/4
        joint_goal[2] = pi/16
        joint_goal[3] = -pi/8
        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        group.go(joint_goal, wait=True)
        # imprimir estado completo del robot
        print("=========EStado del robot")
        print(robot.get_current_state())
        print("")

        # Calling ``stop()`` ensures that there is no residual movement
        group.stop()

        
        input(
            "============ Presiona `Enter` para empezar con planeamiento cartesiano"
        )
        print("========Planeamiento cartesiano")
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.orientation.w = 1.0
        pose_goal.position.x = 0.4
        pose_goal.position.y = 0.1
        pose_goal.position.z = 0.4

        group.set_pose_target(pose_goal)

        # `go()` returns a boolean indicating whether the planning and execution was successful.
        success = group.go(wait=True)
        # Calling `stop()` ensures that there is no residual movement
        group.stop()
        # It is always good to clear your targets after planning with poses.
        # Note: there is no equivalent function for clear_joint_value_targets().
        group.clear_pose_targets()


    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        pass
