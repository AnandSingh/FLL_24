from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.parameters import Stop, Color, Button
from pybricks.tools import wait, multitask, run_task
from TurtleConstant import *
from TurtleHelper import *


class TurtleDrive:
    def __init__(self, ENABLE_GYRO=True, ENABLE_LOGS=False):
        # Initialize both motors. In this example, the motor on the
        # left must turn counterclockwise to make the robot go forward.
        self.left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.B)
        self.log_enabled = ENABLE_LOGS
        # Initialize the drive base. In this example, the wheel diameter is 56mm.
        # The distance between the two wheel-ground contact points is 112mm.
        self.drive_base = DriveBase(
            self.left_motor,
            self.right_motor,
            wheel_diameter=WHEEL_DIAMETER,
            axle_track=AXLE_TRACK,
        )
        self.use_gyro(ENABLE_GYRO)
        self.set_speed_percentage()

        # add attachement motor
        # TODO:

        # add color sensor
        # TODO:
        # self.e_color=ColorSensor(Port.E)
        # self.f_color=ColorSensor(Port.F)

    def log_data(self, note=""):
        if not self.long_enabled:
            return

        time_now = self.watch.time()

        try:
            yaw=self.hub.imu.angle()
            yaw_rate = self.hub.imu.angular_velocity()
        except:
            yaw = None
            yaw_rate = None

        print(time_now, yaw, yaw_rate)



    def stop(self):
        self.drive_base.stop()

    def brake(self):
        self.drive_base.brake()

    def log(self, enable=True):
        self.log_enabled = enable

    def use_gyro(self, enable=True):
        self.drive_base.use_gyro(enable)



    """
    drive the robot straight to spcified distance 
    """

    def straight_drive(self, distance=0, wait=True):
        self.drive_base.straight(distance, then=Stop.HOLD, wait=wait)

    def turn_drive(self, speed, turn_rate, time_millis):
        self.drive_base.drive(speed, turn_rate)
        wait(time_millis)

    """
    Turns the robot to an specified angle
    positive angle turen to the right, negative angle 
    turn to left
    """

    def turn(self, angle, wait=True):
        self.drive_base.turn(angle, then=Stop.HOLD, wait=wait)

    def curve(self, radius, angle, wait=True):
        self.drive_base.curve(radius, angle, then=Stop.HOLD, wait=wait)

    def get_speed_raw(self):
        settings = self.drive_base.settings()
        if self.log_enabled:
            print(
                "speed={}, accel={}, turn_speed={} turn_accel={}".format(
                    settings[0], settings[1], settings[2], settings[3]
                )
            )
        return settings

    def set_speed_raw(
        self,
        speed=DEFAULT_SPEED,
        acceleration=DEFAULT_ACCELERATION,
        turn_rate=DEFAULT_TURN_RATE,
        turn_acceleration=DEFAULT_TURN_ACCELERATION,
    ):
        self.drive_base.settings(speed, acceleration, turn_rate, turn_acceleration)

    """
    Get the speed setting in tuple(straight_speed, straing_aceel, turn_speed, turn_accel)
    """

    def set_speed_percentage(
        self,
        speed_percentage=DEFAULT_SPEED_PERCENTAGE,
        acceleration_percentage=DEFAULT_ACCELERATION_PERCENTAGE,
        turn_rate_percentage=DEFAULT_TURN_RATE_PERCENTAGE,
        turn_acceleration_percentage=DEFAULT_TURN_ACCELERATION_PERCENTAGE,
    ):
        speed = get_speed_mmsec(speed_percentage)
        acceleration = get_acceleration_mmsec2(acceleration_percentage)
        turn_rate = get_turn_rate_degsec(turn_rate_percentage)
        turn_acceleration = get_turn_acceleration_degsec2(turn_acceleration_percentage)
        if self.log_enabled:
            print("\tset speed {}% = {} mm/sec".format(speed_percentage, speed))
            print(
                "\tset accel {}% = {} mm/sec2".format(
                    acceleration_percentage, acceleration
                )
            )
            print(
                "\tset turn_rate {}% = {} deg/sec".format(
                    turn_rate_percentage, turn_rate
                )
            )
            print(
                "\tset turn_accel {}% = {} deg/sec2".format(
                    turn_acceleration_percentage, turn_acceleration
                )
            )
        self.drive_base.settings(speed, acceleration, turn_rate, turn_acceleration)
