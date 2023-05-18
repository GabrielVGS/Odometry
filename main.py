# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from module1 import Odometrium # implementação da odometria para localizar o robo em cordenadas (x,y)

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

v_turn = 20

def rotate(num,velocidade_turn):
    degrees = num * ODO
    tank.on_for_degrees(velocidade_turn, -velocidade_turn, degrees)
    left_motor.wait_while('running', 5000)
    
    tank.stop()

#TODO 

#corrigir a rotação e o andamento do robo por odometria
    
    left_motor.wait_while('running', 5000)
    
    tank.stop()

#TODO 

#corrigir a rotação e o andamento do robo por odometria
    
