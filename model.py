import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self, number, coordinate_x, coordinate_y, coordinate_x0, coordinate_y0, velocity_x, velocity_y, time):
        self.number = number
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.coordinate_x0 = coordinate_x0
        self.coordinate_y0 = coordinate_y0
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.time = time


class Body:
    def __init__(self, points):
        self.points = points


class PointT:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class BodyT:
    def __init__(self, points_t):
        self.points_t = points_t
        self.next_body_t = None
        self.prev_body_t = None


class DoublyLinkedList:
    def __init__(self):
        self.start_body = None

    def insert_in_empty_list(self, points_t):
        if self.start_body is None:
            new_body = BodyT(points_t)
            self.start_body = new_body
        else:
            print("list is not empty")

    def insert_at_end(self, bodies):
        if self.start_body is None:
            new_body = BodyT(bodies)
            self.start_body = new_body
            return
        n = self.start_body
        while n.next_body_t is not None:
            n = n.next_body_t
        new_body = BodyT(bodies)
        n.next_body_t = new_body
        new_body.prev_body_t = n

    def traverse_list(self, j):
        x = []
        y = []
        if self.start_body is None:
            print("List has no element")
            return
        else:
            n = self.start_body
            while n is not None:
                x.append(n.points_t.points_t[j].x)
                y.append(n.points_t.points_t[j].y)
                #print(n.points_t.points_t[j].x)
                n = n.next_body_t
        data = [x, y]
        return data
