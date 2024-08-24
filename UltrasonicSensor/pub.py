#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float64

num = 5.0

class Sensor(Node):
    def __init__(self):
        super().__init__("ultrasonic_sensor")
        self.sensor_reading_pub_= self.create_publisher(Float64,"distance",10)
        self.timer=self.create_timer(1, self.send_sensor_reading)
        

    def send_sensor_reading(self):
        global num
        msg=Float64()
        msg.data=num
        num+=10.0
        self.get_logger().info(f"Sensor read {msg.data}")
        self.sensor_reading_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Sensor()
    rclpy.spin(node)
    rclpy.shutdown()