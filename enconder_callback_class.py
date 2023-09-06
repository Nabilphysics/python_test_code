#!/usr/bin/env python
import rclpy.time
import rclpy
import rclpy.duration
#import roslib
from math import sin, cos, pi

from rclpy.node import Node
from geometry_msgs.msg import Quaternion
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from std_msgs.msg import Int16

class DiffTf:
    def __init__(self):
        self.rate = 10.0
        self.encoder_low_wrap = -13107.2
        self.encoder_high_wrap = 13107.2
        self.encoder_max = 32768
        self.encoder_min = -32768
        self.left = 0
        self.lmult = 0
        self.enc = 0
        self.prev_lencoder = 0

        self.t_delta = rclpy.time.Duration(seconds=1/self.rate)
        print("t_delta: "+ str(self.t_delta))

    def lLowWrapCalculation(self):
        self.result = (self.encoder_max - self.encoder_min) * 0.3 + self.encoder_min
        print("lwrapCalulation+: " + str(self.result))
    
    def lHighWrapCalculation(self):
        self.result = (self.encoder_max - self.encoder_min) * 0.7 + self.encoder_min
        print("lHighWrapCalculation+: " + str(self.result))
    
    def lwheelCallback(self, msg):
    
        enc = msg
        if (enc < self.encoder_low_wrap and self.prev_lencoder > self.encoder_high_wrap):
            self.lmult = self.lmult + 1
            print("lmult+: " + str(self.lmult))
            
        if (enc > self.encoder_high_wrap and self.prev_lencoder < self.encoder_low_wrap):
            self.lmult = self.lmult - 1
            print("lmult-: " + str(self.lmult))
            
        self.left = 1.0 * (enc + self.lmult * (self.encoder_max - self.encoder_min)) 
        print("left: " + str(self.left))
        self.prev_lencoder = enc
        print("prev_lencoder: " + str(self.prev_lencoder))

p = DiffTf()

p.lwheelCallback(14000)
print("p.left:" + str(p.left))
print("------")
p.lwheelCallback(-15000)
print("p.left:" + str(p.left))
print("------")
p.lwheelCallback(-100)
print("p.left:" + str(p.left))


print("------")
d_left = 0
d_right = 0.05
d = (d_left + d_right)/2
th = ( d_right - d_left ) / 0.3048
print("d: " + str(d))
print("th: " + str(th))




     

