WIDTH = 1280
HEIGHT = 800
EPS = 1e-6

BLUE = (255, 0, 0)
RED = (0, 255, 0)
GREEN = (0, 0, 255)
YELLOW = (255, 255, 0)

def init(width, height):
    global WIDTH, HEIGHT
    WIDTH = width
    HEIGHT = height

def s2c_x(s_x):
    """ Convert screen x cord to x cord system. """
    return s_x

def s2c_y(s_y):
    """ On screen y = 0 corresponds to height in cord."""
    return HEIGHT - s_y

def c2s_x(c_x):
    return c_x

def c2s_y(c_y):
    """ On coord y=0 is the height in screen cord. """
    return HEIGHT - c_y

def s2c(s_point):
    """ Convert screen point to coordinate point. """
    return (s2c_x(s_point[0]), s2c_y(s_point[1]))

def c2s(c_point):
    """ Convert coordinate point to screen point. """
    return (c2s_x(c_point[0]), c2s_y(c_point[1]))