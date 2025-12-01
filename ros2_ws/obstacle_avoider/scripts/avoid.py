#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math
import random

class LunarAvoider(Node):
    def __init__(self):
        super().__init__('lunar_avoidance')

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.safe_distance = 0.9   # meters
        self.forward_speed = 0.4
        self.turn_speed = 0.7

        self.timer = self.create_timer(0.1, self.control_loop)
        self.obstacle = False
        self.turn_dir = 1

        self.get_logger().info("✅ Obstacle Avoidance Started")

    def scan_callback(self, scan):
        center = len(scan.ranges) // 2
        front = scan.ranges[center-15:center+15]

        if min(front) < self.safe_distance:
            self.obstacle = True
            self.turn_dir = random.choice([-1,1])
        else:
            self.obstacle = False

    def control_loop(self):
        msg = Twist()

        if self.obstacle:
            msg.linear.x = 0.0
            msg.angular.z = self.turn_speed * self.turn_dir
        else:
            msg.linear.x = self.forward_speed
            msg.angular.z = 0.0

        self.cmd_pub.publish(msg)


def main():
    rclpy.init()
    node = LunarAvoider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

