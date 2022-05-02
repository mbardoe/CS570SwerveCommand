import math

from pose2d import Pose2D


def SwerveCommand(origin: Pose2D, target: Pose2D, max_linear_speed, max_angular_speed, speed):
    """"SwerveCommmand takes in 2 poses and returns a tuple of time, and 4 directions and speeds for the 4 wheels
    of a swerve drive robot. The speed is a percentage of the max speed to go."""

    return time, left_front_direction, right_front_direction, left_back_direction, right_back_direction, \
           left_front_speed, right_front_speed, left_back_speed, right_back_speed


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pose1 = Pose2D(4, 1, 0)
    pose2 = Pose2D(5, 2, 1)
    print(SwerveCommand(pose1, pose2, math.pi, math.sqrt(2) * math.pi), .3)

# Answers should be:
# time=1.5005
# left_front_direction =-1.249045
# right_front_direction = -0.785398
# left_back_direction = -0.785398
# right_back_direction = -0.3217505
# the speed numbers are different from our calculations in class because we now report them as a fraction of the max.
# left_front_speed = 0.33541019  # the speed numbers are different from our calculations in class be
# right_front_speed = 0.15
# left_back_speed = 0.45
# right_back_speed = 0.335410196
