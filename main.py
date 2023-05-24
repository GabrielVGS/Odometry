import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *
from odometrium import *
from utils import *

from time import sleep

# left='B'                  the left wheel is connected to port B
# right='C'                 the right wheel is connected to port C
# wheel_diameter=5.5        the wheel diameter is 5.5cm
# wheel_distance=12         the wheel distance is 12cm
# unit sidenote: as long as you are consistent, you can also use mm, inches, km.
# returned values are in these units
# counts per rotation are is the number of motor-internal 'tacho-counts'
# that the motor has to travel for one full revolution
# this is motor specific
#
# count_per_rot_left=None   use the default value returned by the motor for the left motor
# count_per_rot_right=360   for the right motor treat 360 tacho counts as one full revolution
# debug=False               print the current position (on motor speed change) and
#                           echo all the movement logs when the object is destroyed
# curve_adjustment=0.873    use curve adjustment factor of 0.873, see below ('percision')  
robot = Robot(OUTPUT_A,OUTPUT_B)
robot.rotate(90,100,20)
