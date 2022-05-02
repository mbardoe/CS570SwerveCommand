import math

from pose2d import Pose2D


def SwerveCommand(origin: Pose2D, target: Pose2D, max_linear_speed, max_angular_speed, track_width, speed):
    """"SwerveCommmand takes in 2 poses and returns a tuple of time, and 4 directions for the 4 wheels
    of a swerve drive robot. The speed is a percentage of the max speed to allow. """
    delta_x = target.x - origin.x
    delta_y = target.y - origin.y

    movement_angle = math.atan2(delta_y, delta_x)

    distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
    rotation = target.theta - origin.theta

    time_move = distance / (max_linear_speed * speed)
    time_twist = math.fabs(rotation / (max_angular_speed * speed))

    time = max(time_move, time_twist)
    linear_slow_down = time_move / time
    twist_slow_down = time_twist / time

    movement_vector = [speed * linear_slow_down * math.cos(movement_angle),
                       speed * linear_slow_down * math.sin(movement_angle)]

    left_front_twist = [speed * twist_slow_down * math.cos(5 * math.pi / 4),
                        speed * twist_slow_down * math.sin(5 * math.pi / 4)]
    right_front_twist = [speed * twist_slow_down * math.cos(3 * math.pi / 4),
                         speed * twist_slow_down * math.sin(3 * math.pi / 4)]
    left_back_twist = [speed * twist_slow_down * math.cos(7 * math.pi / 4),
                       speed * twist_slow_down * math.sin(7 * math.pi / 4)]
    right_back_twist = [speed * twist_slow_down * math.cos(1 * math.pi / 4),
                        speed * twist_slow_down * math.sin(1 * math.pi / 4)]

    left_front_direction, left_front_speed = direction_and_speed(left_front_twist[0] + movement_vector[0],
                                                                 left_front_twist[1] + movement_vector[1])
    right_front_direction, right_front_speed = direction_and_speed(right_front_twist[0] + movement_vector[0],
                                                                   right_front_twist[1] + movement_vector[1])
    left_back_direction, left_back_speed = direction_and_speed(left_back_twist[0] + movement_vector[0],
                                                               left_back_twist[1] + movement_vector[1])
    right_back_direction, right_back_speed = direction_and_speed(right_back_twist[0] + movement_vector[0],
                                                                 right_back_twist[1] + movement_vector[1])

    return time, left_front_direction, right_front_direction, left_back_direction, right_back_direction, \
           left_front_speed, right_front_speed, left_back_speed, right_back_speed


def direction_and_speed(horizontal_speed, vertical_speed):
    return math.atan2(vertical_speed, horizontal_speed), math.sqrt(horizontal_speed ** 2 + vertical_speed ** 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pose1 = Pose2D(4, 1, 0)
    pose2 = Pose2D(5, 2, 1)
    print(SwerveCommand(pose1, pose2, math.pi, math.sqrt(2) * math.pi))
