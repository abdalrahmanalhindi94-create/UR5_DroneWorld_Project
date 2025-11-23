#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class URBackAndForthFast(Node):
    def __init__(self):
        super().__init__("ur_back_and_forth_fast")

        # ⚠️ Change this if your controller topic is different
        topic = "/scaled_joint_trajectory_controller/joint_trajectory"
        self.pub = self.create_publisher(JointTrajectory, topic, 10)

        # UR arm joint order
        self.joint_names = [
            "shoulder_pan_joint",
            "shoulder_lift_joint",
            "elbow_joint",
            "wrist_1_joint",
            "wrist_2_joint",
            "wrist_3_joint",
        ]

        # Pose A: upright "home" pose
        self.pose_home = [0.0, -1.57, 1.57, -1.57, -1.57, 0.0]

        # Pose B: rotated pose (clear, visible difference)
        self.pose_rot = [1.5, -1.5, 1.5, -1.0, 1.5, 0.0]

        # Start by moving from home -> rotated
        self.go_to_rotated = True

        # Send new motion every 4 seconds (faster switching)
        self.timer = self.create_timer(4.0, self.send_next_trajectory)

        self.get_logger().info(
            "URBackAndForthFast started. First fast move in ~4 seconds."
        )

    def send_next_trajectory(self):
        if self.go_to_rotated:
            target = self.pose_rot
            label = "ROTATED"
        else:
            target = self.pose_home
            label = "HOME"

        msg = JointTrajectory()
        msg.joint_names = self.joint_names

        point = JointTrajectoryPoint()
        point.positions = target
        # Faster movement (reach target in 2 seconds)
        point.time_from_start = Duration(sec=2, nanosec=0)
        msg.points.append(point)

        self.pub.publish(msg)
        self.get_logger().info(f"Trajectory sent to {label} pose.")
        self.go_to_rotated = not self.go_to_rotated

def main(args=None):
    rclpy.init(args=args)
    node = URBackAndForthFast()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
