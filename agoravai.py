# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from odometrium import Odometrium

# Create the sensors and motors objects
left_motor = LargeMotor(OUTPUT_A)
right_motor = LargeMotor(OUTPUT_B)
left_motor.stop_action = "hold"
right_motor.stop_action = "hold"

pos_info = Odometrium(left='A',right="B",wheel_diameter=5.6,wheel_distance=15.2,
                      count_per_rot_left=None,count_per_rot_right=360,debug=False,
                      curve_adjustment=1)


pos_info.move(left=50,right=50,time=3)


