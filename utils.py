from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from odometrium import *
import math


class Robot(MoveSteering):
    def __init__(self,left_motor_port,right_motor_port,wheel_distance = 15.2,wheel_dm = 5.6,desc=None,motor_class=LargeMotor):
        MoveSteering.__init__(self, left_motor_port, right_motor_port, desc, motor_class)
        self.wheel_distance = wheel_distance
        self.wheel_dm = wheel_dm
        self.wheel_circumference = wheel_dm * math.pi
        self.C = self.wheel_distance * math.pi
        #GYRO
        self._gyro = None

        # Odometria
        self.pos_info = Odometrium(left='B', right='C', wheel_diameter=5.6, wheel_distance=15.2,
                      count_per_rot_left=None, count_per_rot_right=360, debug=False,
                      curve_adjustment=.873)
        

        self.left_motor = LargeMotor(left_motor_port)
        self.right_motor = LargeMotor(right_motor_port)


    def on_for_distance(self,steering,speed,distance,brake=True,block = True):
        rotations = distance / self.wheel_circumference
        MoveSteering.on_for_rotations(self,steering,speed,rotations,brake,block)

    def rotate(self,n,steering,v):
        arc = (n) * self.C
        degrees = (arc/self.wheel_circumference)
        MoveSteering.on_for_degrees(self,steering,v,degrees)
        self.left_motor.wait_while('running', 5000)
        MoveSteering.stop(self)

    def move(self,distance,direction,v,use_gyro = True,factor = 10):
        degrees = (distance/self.wheel_circumference) * 360
        target = self.left_motor.position + degrees

        if use_gyro:
            while self.left_motor.position <= target:
                error = (direction - self._gyro.angle) * factor
                error = max(min(error,100), -100) #Corrige pra não passar do intervalo [-100,100]
                MoveSteering.on(self,error,v)
            MoveSteering.stop(self)

        else:
            raise NotImplementedError 
 
