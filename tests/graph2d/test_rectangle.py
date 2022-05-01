import unittest
from golfswing.graph2d import screen, line, draw
from golfswing.graph2d import parallelogram

class TestParallelogram(unittest.TestCase):
    def setUp(self):
        self.width = 1280
        self.height = 800
        screen.init(width=self.width, height=self.height)

    def test_rectangle1(self):
        r1 = parallelogram.make_rectangle((0, 0), 10, 20)
        self.assertEqual(r1.vertices[0], (0, 0))
        self.assertEqual(r1.vertices[1], (0, 20))
        self.assertEqual(r1.vertices[2], (10, 20))
        self.assertEqual(r1.vertices[3], (10, 0))


    def test_intersect1(self):
        r1 = parallelogram.make_rectangle((100, 100), 300, 500)
        l1 = line.Line((10, 300), (300, 300))
        points = r1.intersect_line(l1)
        self.assertEqual(points[0], (100, 300))
        self.assertEqual(points[1], None)
        self.assertEqual(points[2], (400, 300))
        self.assertEqual(points[3], None)

    def test_no_intersect(self):
        r1 = parallelogram.make_rectangle((100, 100), 300, 500)
        l2 = line.Line((10, 700), (300, 700))
        points = r1.intersect_line(l2)
        self.assertEqual(points[0], None)
        self.assertEqual(points[1], None)
        self.assertEqual(points[2], None)
        self.assertEqual(points[3], None)