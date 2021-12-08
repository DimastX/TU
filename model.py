class Point:
    def __init__(self, number, coordinate_x, coordinate_y, coordinate_x0, coordinate_Y0, Velocity_x, Velocity_y, time):
        self.number = number
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.coordinate_x0 = coordinate_x0
        self.coordinate_y0 = coordinate_Y0
        self.velocity_x = Velocity_x
        self.velocity_y = Velocity_y
        self.time = time


class Body:
    def __init__(self, points):
        self.points = points


class PointT:
    def __init__(self, point, x, y):
        self.point = point
        self.x = x
        self.y = y


class BodyT:
    def __init__(self, points_t):
        self.points_t = points_t
