"""
Draw utility class.
"""
import cv2

from golfswing.graph2d import screen
from golfswing.graph2d.line import VerticalLine
from golfswing.graph2d.line_style import Target, Default, Club, Plane
from golfswing.graph2d.parallelogram import Parallelogram

def join(img, points, style="", color=(255, 0, 0), thickness=5):
    """
    Join all the points in the array with a line.
    :param img: image to draw on
    :param points: list of points in screen co ordinate.
    :param style: Either dotted or filled
    :param color: Color in BGR triplet format.
    :param thickness: Pixed width of the line.
    :return: None, the image is updated.
    """
    if len(points) < 2:
        return
    for i in range(len(points) - 1):
        if style == "dotted":
            if i % (thickness + 5) == 0:
                cv2.circle(img, points[i], thickness, color, -1)
        else:
            cv2.line(img, points[i], points[i + 1], color=color, thickness=thickness)

def line_from(img, line, x1, x2, line_style=Default):
    """
    Draw a line from x1 screen cord to x2 screen co ord
    :param img: Image to draw the line.
    :param line:  Equation of a line
    :param x1: Initial point x
    :param x2: Final point x
    :param line_style: Line style
    :return: None
    """
    points = line.s_points(x1, x2)
    join(img, points, style=line_style.style, thickness=line_style.thickness,
         color = line_style.color)


def target_line(img, point):
    """ A target line is a vertical line from ball to target. """
    v1 = VerticalLine(point[0])
    line_from(img, v1, 0, screen.HEIGHT, Target)


def club_line(img, line, x1, x2):
    line_from(img, line, x1, x2, Club)


def swing_plane(img, plane):
    """
    Draw a parallelogram using the points.
    """
    points = plane.s_points()

    join(img, points, style=Plane.style,
         thickness=Plane.thickness,
         color=Plane.color)
