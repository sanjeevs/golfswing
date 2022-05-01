from golfswing.graph2d import line, utils

class Parallelogram:
    def __init__(self, p1, p2, p3, p4):
        # Like to arrange the vertices in left, top, right, bottom order.
        lst = [p1, p2, p3, p4]
        self.vertices = sorted(lst, key=lambda x: x[1])
        self.vertices = sorted(lst, key=lambda x: x[0])
        tmp = self.vertices[2]
        self.vertices[2] = self.vertices[3]
        self.vertices[3] = tmp

        self.lines = [None] * 4
        self.lines[0]= line.Line(self.vertices[0], self.vertices[1])
        self.lines[1] = line.Line(self.vertices[1], self.vertices[2])
        self.lines[2]= line.Line(self.vertices[2], self.vertices[3])
        self.lines[3] = line.Line(self.vertices[3], self.vertices[0])

    def s_points(self):
        return [self.vertices[0], self.vertices[1], self.vertices[2],
                self.vertices[3], self.vertices[0]]

    def intersect_line(self, line):
        """
        Find the intersection of a line and parallelogram.
        :param line:
        :return: A tuple of 4 members.
                 Each entry is a intersection point with the corresponding line.
                 None if there is no intersection.
        """
        intersects = []
        for i in range(4):
            intersect = self.lines[i].intersect_point(line)
            if intersect is not None:
                if utils.is_point_between(intersect, self.vertices[0], self.vertices[1]) \
                    or utils.is_point_between(intersect, self.vertices[1], self.vertices[2]) \
                    or utils.is_point_between(intersect, self.vertices[2], self.vertices[3]) \
                    or utils.is_point_between(intersect, self.vertices[3], self.vertices[0]) :
                        intersects.append(intersect)
                else:
                    intersects.append(None)
            else:
                intersects.append(None)

        return intersects

# Factory Constructor
def make_parallelogram(pt1, pt2, pt3):
    """
    Draw a parallelogram using the points.
    :param pt1: Vertex of parallelogram
    :param pt2: Corresponding vertex of parallelogram.
    :param pt3: Any point on the opposite side of the parallelogram.
    :return: parallelogram
    """
    l1 = line.Line(pt1, pt2)
    l2 = line.PrependicularLine(l1, pt2)
    l3 = line.ParallelLine(l1, pt3)
    l4 = line.PrependicularLine(l1, pt1)

    vertex1 = l2.intersect_point(l3)
    vertex2 = l3.intersect_point(l4)

    p = Parallelogram(pt1, pt2, vertex1, vertex2)
    return p


def make_rectangle(pt, width, height):
    """
    make a rectangle.
    :param pt:
    :param width:
    :param height:
    :return: rectangle
    """
    pt2 = (pt[0] + width, pt[1])
    pt3 = (pt[0], pt[1] + height)
    return make_parallelogram(pt, pt2, pt3)