from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from odometrium import *
import math


class Robot(MoveSteering):
    def __init__(self,left_motor_port,right_motor_port,wheel_distance = 15.2,wheel_dm = 5.6,desc=None,motor_class=LargeMotor):
        MoveTank.__init__(self, left_motor_port, right_motor_port, desc, motor_class)
        self.wheel_distance = wheel_distance
        self.wheel_dm = wheel_dm
        self.odo = self.wheel_distance / self.wheel_dm
        self.wheel_circumference = wheel_dm * math.pi
        self._gyro = None
        self.pos_info = Odometrium(left='B', right='C', wheel_diameter=5.6, wheel_distance=15.2,
                      count_per_rot_left=360, count_per_rot_right=360, debug=True,
                      curve_adjustment=.873)
        

        self.theta = self.pos_info.orientation
        self.x = self.pos_info.x
        self.y = self.pos_info.y
        self.left_motor = LargeMotor(left_motor_port)
        self.right_motor = LargeMotor(right_motor_port)


    def on_for_distance(self,steering,speed,distance,brake=True,block = True):
        rotations = distance / self.wheel_circumference
        MoveSteering.on_for_rotations(self,steering,speed,rotations,brake,block)

    def rotate(self,n,steering,v):
        C = self.wheel_distance * math.pi
        arc = (n) * C
        degrees = (arc/self.wheel_circumference)
        MoveSteering.on_for_degrees(self,steering,v,degrees)
