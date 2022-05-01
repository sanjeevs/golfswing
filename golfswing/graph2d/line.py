from golfswing.graph2d import screen


class Line:
    """
        Represent a line a point in coordinate system and slope.
    """

    def __init__(self, s_pt1, s_pt2):
        self.pt1 = screen.s2c(s_pt1)
        pt2 = screen.s2c(s_pt2)

        run = self.pt1[0] - pt2[0]
        if abs(run) <= screen.EPS:
            self.vertical = True
        else:
            self.vertical = False
            self.slope = (self.pt1[1] - pt2[1]) / run;

    def y_cord(self, x):
        """ Return the y coordinate of the point given the x value in coord system."""
        if self.vertical:
            return self.pt1[1]
        else:
            return self.slope * (x - self.pt1[0]) + self.pt1[1]

    def s_points(self, s_x1, s_x2):
        """ Return a list of screen points between the x screen interval. """
        points = []
        y = 0
        xmin = screen.s2c_x(s_x1)
        xmax = screen.s2c_x(s_x2)

        if xmax < xmin:
            xmax, xmin = xmin, xmax

        for x in range(xmin, xmax):
            if self.vertical:
                points.append((self.pt1[0], y))
                y += 1
            else:
                y = self.y_cord(x)
                points.append((x, round(y)))

        # Convert back to screen coordinates
        return [screen.c2s(i) for i in points]

    def intersect_point(self, line):
            """ Return the point of intersection of 2 lines.
                If lines are parallel then return None.
                If lines are same, ie infinite solution then return None
                :param line : Line object
            """
            intersect = None
            y1_intercept = self.y_cord(0)
            y2_intercept = line.y_cord(0)

            if self.vertical and line.vertical:
                return None

            if self.vertical ^ line.vertical:
                if self.vertical:
                    x1 = screen.c2s_x(self.pt1[0])
                    y1 = screen.c2s_y(line.y_cord(self.pt1[0]))
                    return (round(x1), round(y1))
                else:
                    x1 = screen.c2s_x(line.pt1[0])
                    y1 = screen.c2s_y(self.y_cord(line.pt1[0]))
                    return (round(x1), round(y1))
            else:
                diff_slope = self.slope - line.slope
                if abs(diff_slope) <= screen.EPS:
                    # Lines are parallel
                    return None
                else:
                    x = (y2_intercept - y1_intercept)/(self.slope - line.slope)
                    y = self.y_cord(x)
                    return screen.c2s((round(x), round(y)))


class VerticalLine(Line):
    """ Vertical line passing through a x point. """
    def __init__(self, s_x):
        self.pt1 = screen.s2c((s_x, 0))
        self.vertical = True


    def s_points(self, s_y1, s_y2):
        points = []
        ymin = screen.s2c_y(s_y1)
        ymax = screen.s2c_y(s_y2)
        if ymax < ymin:
            ymax, ymin = ymin, ymax
        self.vertical = True

        for y in range(ymin, ymax):
            points.append((int(self.pt1[0]), y))

        return [screen.c2s(i) for i in points]

class ParallelLine(Line):
    """ A line parallel to a line and passes through a point in screen co ordindate. """
    def __init__(self, line, s_point):
        self.pt1 = screen.s2c(s_point)
        self.vertical = line.vertical
        if not self.vertical:
            self.slope = line.slope


class PrependicularLine(Line):
    """ A line that is prependicular to the given line and passing a point. """
    def __init__(self, line, s_point):
        if line.vertical:
            self.vertical = False
            self.slope = 0
            self.pt1 = (screen.s2c(s_point))

        elif line.slope == 0:
            self.vertical = True
            self.pt1 = (screen.s2c((s_point[0], 0)))

        else:
            self.vertical = False
            self.slope = -1 * (1 / line.slope)
            self.pt1 = (screen.s2c_x(s_point[0]), line.y_cord(screen.s2c_x(s_point[0])))
