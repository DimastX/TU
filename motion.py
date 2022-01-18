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
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()
    ax.set(title='Траектория',
           xlabel='x',
           ylabel='y')
    for i in range(n):
        data.append(trajectory.traverse_list(i))
        plt.plot(data[i][0], data[i][1], label=str(i)+'-ая точка')
        xpoint = [data[i][0][0]]
        ypoint = [data[i][1][0]]
        ax.scatter(xpoint, ypoint, color='green', marker='*')
        xpoint = [data[i][0][len(data[i][0])-1]]
        ypoint = [data[i][1][len(data[i][1])-1]]
        ax.scatter(xpoint, ypoint, color='red', marker='*')
        i += 1
    #print(data[i][0][0])
    #ax.legend()
    plt.show()
    #plt.savefig('plots/trajectory' + '.png', format='png', dpi=1200)


def velocity_fields(time, dt, border, w):
    t = dt
    vf = [] #velocity fields
    k = 0
    a = np.linspace(-border, border, 2 * border + 1)
    x_k, y_k = np.meshgrid(a, a)
    for n in range (int(time/dt)):
        plt.figure(n)
        plt.suptitle('t = ' + str(t))
        points = []
        for i in range(2 * border + 1):
            for j in range(2 * border + 1):
                x = x_k[i, j]
                y = y_k[i, j]
                points.append(model.Point(k, x, x, x, x, f_x(t, x), f_y(t, y, w), t))
                k += 1
                plt.subplot(1, 2, 1)
                plt.quiver(x, y, f_x(t, x), f_y(t, y, w))
        vf.append(model.Body(points))
        for p in range(1, 4):
            for q in range(1, 4):
                x = np.linspace(-4, -0.1, 100)
                d = math.exp(t) / math.log(t + 1)
                c = q * (p ** d)
                y = -c * ((-x) ** (-d))
                plt.subplot(1, 2, 2)
                plt.axis([-4, 4, -4, 4])
                plt.plot(x, y)
        t += dt
        #plt.show()
        plt.savefig('plots/velocity_fields' + str(n) + '.png', format='png', dpi=1200)
    return vf
