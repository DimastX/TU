import model
import math
import matplotlib.pyplot as plt
import numpy as np


def f_x(t, x):
    return math.exp(t) * x
    #return t


def f_y(t, y, w):
    return math.cos(w * t) * y
    #return t


def body_init(x_c, y_c, r, w, n):
    points = []
    i = 0
    t = 0
    m = n / 2 #
    for k in range(n):
        x = x_c + math.cos(k * r * math.pi / m)
        y = y_c + math.sin(k * r * math.pi / m)
        points.append(model.Point(i, x, y, x, y, f_x(t, x), f_y(t, y, w), t))
        i += 1
    return model.Body(points)


def int_runge_x(x, t, h):
    f_1 = f_x(t, x)
    f_2 = f_x(t + h * 2/3, x + h * f_1 * 2/3)
    f_3 = f_x(t + h * 2/3, x - h * f_1 * 1/3 + h * f_2)
    return x + h/4 * (f_1 + 2 * f_2 + f_3)


def int_runge_y(y, t, h, w):
    f_1 = f_y(t, y, w)
    f_2 = f_y(t + h * 2/3, y + h * f_1 * 2/3, w)
    f_3 = f_y(t + h * 2/3, y - h * f_1 * 1/3 + h * f_2, w)
    return y + h/4 * (f_1 + 2 * f_2 + f_3)


def trajectory(time, dt, body, w, n):
    body_stat = []
    t = 0
    i = 0
    data = []
    trajectory = model.DoublyLinkedList()
    while t < time:
        for j in range(len(body.points)):
            x = body.points[j].coordinate_x0
            y = body.points[j].coordinate_y0
            #body_stat.append(model.PointT(body.points[j].coordinate_x0, body.points[j].coordinate_y0))
            body_stat.append(model.PointT(int_runge_x(x, t, dt), int_runge_y(y, t, dt, w)))
            j += 1
        body_t = model.BodyT(body_stat)
        t += dt
        trajectory.insert_at_end(body_t)
        j = 0
        body_stat = []