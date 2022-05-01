import unittest
from golfswing.graph2d import screen, line, draw
from golfswing.graph2d import parallelogram

class TestParallelogram(unittest.TestCase):
    def setUp(self):
        self.width = 1280
        self.height = 800
        screen.init(width=self.width, height=self.height)

    def test_intersect_l0_l2(self):
        pt1 = ( 10, 10)
        pt2 = ( 10, 20)
        pt3 = (20, 30)
        p1 = parallelogram.make_parallelogram(pt1, pt2, pt3)
        l1 = line.Line((0, screen.HEIGHT // 2), (screen.WIDTH // 2,
                                                 screen.HEIGHT // 2))

        intersects = p1.intersect_line(l1)
        self.assertEqual(len(intersects), 4)
