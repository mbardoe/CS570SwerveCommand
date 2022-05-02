import math

from pose2d import Pose2D


def SwerveCommand(origin: Pose2D, target: Pose2D, max_linear_speed, max_angular_speed, track_width, speed):
    """"SwerveCommmand takes in 2 poses and returns a tuple of time, and 4 directions for the 4 wheels
    of a swerve drive robot. The speed is a percentage of the max speed to allow. """
    delta_x=target.x-origin.x
    detla_y=target.y-orgin.y

    distance=math.sqrt(delta_x**2 + delta_y**2)
    rotation=target.theta-origin.theta

    time_move=distance/max_linear_speed
    time_twist=math.fabs(rotation/max_angular_speed


    return time, left_front_direction, right_front_direction, left_back_direction, right_back_direction


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pose1=Pose2D(4,1,0)
    pose2=Pose2D(5,2,1)
    print(SwerveCommand(pose1, pose2, math.pi, math.sqrt(2)*math.pi))

