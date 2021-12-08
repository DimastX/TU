import model
import math
import matplotlib.pyplot as plt
import numpy as np


def f_x(t, x):
    return math.exp(t) * x


def f_y(t, y, w):
    return math.cos(w * t) * y


def body_init(x_c, y_c, r, w):
    points = []
    i = 0
    t = 0
    for n in range(8):
        x = x_c + math.cos(n * r * math.pi / 4)
        y = y_c + math.sin(n * r * math.pi / 4)
        points.append(model.Point(i, x, y, x, y, f_x(t, x), f_y(t, y, w), t))
        i += 1
    return model.Body(points)
