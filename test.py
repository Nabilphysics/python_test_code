#! /usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):

   def __init__(self):
       super().__init__("nabil_first_node")
       # node name : first_node but this file name my_first_node
       # remember executable name may be different in setup.py file
       self.counter_ = 1
       # This node first print the following line
       self.get_logger().info("Hello from nabil_first_node")
       # This timer will call timer_callback function in every 0.5 Second
       self.create_timer(0.5, self.timer_callbac)

   def timer_callbac(self):
       self.get_logger().info("www.nabilbd.com " + "Counter: " + str(self.counter_))
       self.counter_ = self.counter_ + 1
       #self.t_delta = rclpy.time.Duration(seconds=1/10)
       self.t_delta = 0.1
       self.time_now[0] = self.get_clock().now().seconds_nanoseconds() 
       self.t_next = self.time_now[0]  + self.t_delta
       self.timbomb = self.get_clock().now().seconds_nanoseconds()
       print(self.t_next[0])
     
       


def main(args = None):
   # Start the node
   rclpy.init(args = args)
   
   node = MyNode()
   # spin will keep the node running
   rclpy.spin(node) 
   
   # Finally Shutdown the node
   rclpy.shutdown()


if __name__ == '__main__':
   main()