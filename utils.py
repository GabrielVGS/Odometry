from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from gyro import GyroSensor
import math

class Robot(MoveTank):
    def __init__(self,left_motor_port,right_motor_port,wheel_distance_mm,wheel_dm = 56,desc=None,motor_class=LargeMotor):
        MoveTank.__init__(self, left_motor_port, right_motor_port, desc, motor_class)
        self.wheel_distance_mm = wheel_distance_mm
        self.wheel_circumference_mm = wheel_dm * math.pi
        self._gyro = None
    @property
    def gyro(self):
        return self._gyro
    

    @gyro.setter
    def gyro(self, gyro):
        self._gyro = gyro


    def on_for_distance(self,speed,distance_mm,brake=True,block = False):
        rotations = distance_mm / self.wheel_circumference_mm
        MoveTank.on_for_rotations(self,speed,speed,rotations,brake,block)
              
    def turn_degrees(self, speed, degrees, brake=True, block = True,error_margin = 2, sleep_time=0.01,use_gyro=True):
        def final_angle(init_angle, degrees):
            result = init_angle - degrees

            while result <= -360:
                result += 360

            while result >= 360:
                result -= 360

            if result < 0:
                result += 360

            return result

        # use the gyro to check that we turned the correct amount?
        use_gyro = bool(use_gyro and block and brake)
        if use_gyro and not self._gyro:
            raise ValueError(
                "The 'gyro' variable must be defined with a GyroSensor. Example: tank.gyro = GyroSensor()")

        if use_gyro:
            angle_init_degrees = self._gyro.circle_angle()
        else:
            angle_init_degrees = math.degrees(self.theta)

        angle_target_degrees = final_angle(angle_init_degrees, degrees)


        # The distance each wheel needs to travel
        distance_mm = (abs(degrees) / 360) * self.circumference_mm

        # The number of rotations to move distance_mm
        rotations = distance_mm / self.wheel.circumference_mm

        # If degrees is positive rotate clockwise
        if degrees > 0:
            MoveTank.on_for_rotations(self, speed, speed * -1, rotations, brake, block)

        # If degrees is negative rotate counter-clockwise
        else:
            MoveTank.on_for_rotations(self, speed * -1, speed, rotations, brake, block)

        if use_gyro:
            angle_current_degrees = self._gyro.circle_angle()

            # This can happen if we are aiming for 2 degrees and overrotate to 358 degrees
            # We need to rotate counter-clockwise
            if 90 >= angle_target_degrees >= 0 and 270 <= angle_current_degrees <= 360:
                degrees_error = (angle_target_degrees + (360 - angle_current_degrees)) * -1

            # This can happen if we are aiming for 358 degrees and overrotate to 2 degrees
            # We need to rotate clockwise
            elif 360 >= angle_target_degrees >= 270 and 0 <= angle_current_degrees <= 90:
                degrees_error = angle_current_degrees + (360 - angle_target_degrees)

            # We need to rotate clockwise
            elif angle_current_degrees > angle_target_degrees:
                degrees_error = angle_current_degrees - angle_target_degrees

            # We need to rotate counter-clockwise
            else:
                degrees_error = (angle_target_degrees - angle_current_degrees) * -1

            log.info("%s: turn_degrees() ended up at %s, error %s, error_margin %s" %
                     (self, angle_current_degrees, degrees_error, error_margin))

            if abs(degrees_error) > error_margin:
                self.turn_degrees(speed, degrees_error, brake, block, error_margin, use_gyro)
