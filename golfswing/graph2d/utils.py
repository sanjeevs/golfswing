import math
from golfswing.graph2d import screen

def distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

def is_point_between(pt, pt1, pt2):
    diff =  distance(pt1, pt2) - (distance(pt1, pt) + distance(pt2, pt))
    return (abs(diff) < screen.EPS)

def create_bounding_box(point, length):
    return (point[0], point[1], length, length)
