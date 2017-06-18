import math

def split_speed(speed, direction):
    all_sum = direction[0] + direction[1]
    x = direction[0] / all_sum
    y = direction[1] / all_sum

    return (x, y)
