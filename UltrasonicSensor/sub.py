#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float64

class Reciever(Node):
    def __init__(self):
        super().__init__("ultrasonic_reciever")
        self.pose_subscriber=self.create_subscription(Float64,"distance",self.pose_callback,10)


    def pose_callback(self,msg:Float64):
        if (msg.data<70):
            self.get_logger().info("DISTANCE: "+str(msg.data)+" (CRITICAL)")
        else:
            self.get_logger().info("DISTANCE: "+str(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = Reciever()
    rclpy.spin(node)
    rclpy.shutdown()