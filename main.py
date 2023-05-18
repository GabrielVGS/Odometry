# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from odometrium import Odometrium # implementação da odometria para localizar o robo em cordenadas (x,y)

#https://github.com/sterereo/odometrium/tree/master <- documentação 


# Create the sensors and motors objects
left_motor = LargeMotor(OUTPUT_A)
right_motor = LargeMotor(OUTPUT_B)
left_motor.stop_action = "hold"
right_motor.stop_action = "hold"
tank = MoveTank(OUTPUT_A,OUTPUT_B)
pos_info = Odometrium(left='A',right="B",wheel_diameter=5.6,wheel_distance=15.2,
                      count_per_rot_left=None,count_per_rot_right=360,debug=False,
                      curve_adjustment=1)


ODO = 15.2/5.6

v_turn = 35

def rotate(num):
    degrees = num * ODO
    tank.on_for_degrees(velocidade_turn, -velocidade_turn, degrees)
    
    left_motor.wait_while('running', 5000)
    
    tank.stop()
 
while True:
  pos_info.move(right = 500,left = 500, time = 5)
  time.sleep(0.5)
  rotate(90)

