import unittest
from golfswing.graph2d import screen, line, draw

class TestScreen(unittest.TestCase):
    def setUp(self):
        self.width = 1280
        self.height = 800
        screen.init(width=self.width, height=self.height)

    def test_screen(self):
        self.assertEqual(self.width, screen.WIDTH)
        self.assertEqual(self.height, screen.HEIGHT)
        
    def test_line1(self):
        l1 = line.Line((0, 0), (self.width, self.height))
        self.assertFalse(l1.vertical)
        self.assertAlmostEqual(l1.slope, -self.height/self.width, 3)

    def test_vertical_line(self):
        l1 = line.Line((0, 0), (0, 400))
        self.assertTrue(l1.vertical)

    def test_prependicular_line(self):
        l1 = line.Line((0, 0), (self.width, self.height))
        l2 = line.PrependicularLine(l1, (0, 0))
        self.assertEqual(l2.slope, -1/(l1.slope))

    def test_prependicular_line_x(self):
        l1 = line.Line((0, 0), (self.width, 0))
        l2 = line.PrependicularLine(l1, (100, 200))
        intersect = l2.intersect_point(l1)
        self.assertEqual(intersect[0], 100)
        self.assertEqual(intersect[1], 0)

    def test_prependicular_line_y(self):
        l1 = line.Line((100, 0), (100, self.height))
        l2 = line.PrependicularLine(l1, (100, 200))
        print(l2.pt1)
        intersect = l2.intersect_point(l1)
        self.assertEqual(l2.slope, 0)
        self.assertEqual(intersect[0], 100)
        self.assertEqual(intersect[1], 200)

    def test_parallel_line(self):
        l1 = line.Line((0, 0), (self.width, self.height))
        l2 = line.ParallelLine(l1, (10, 10))
        self.assertEqual(l2.slope, l1.slope)

    def test_intersect_center(self):
        l1 = line.Line((0, 0), (self.width, self.height))
        l2 = line.Line((self.width, 0), (0, self.height))
        point = draw.intersect_point(l1, l2)
        self.assertAlmostEqual(point[0], self.width/2, 3)
        self.assertAlmostEqual(point[1], self.height/2, 3)

    def test_intersect_none(self):
        l1 = line.Line((0, 0), (self.width, self.height))
        self.assertIsNone(l1.intersect_point(l1))

    def test_intersect_center(self):
        l1 = line.Line((0, 0), (self.width, self.height))
        l2 = line.Line((self.width, 0), (0, self.height))
        intersect = l1.intersect_point(l2)
        self.assertEqual(intersect[0], self.width // 2)
        self.assertEqual(intersect[1], self.height // 2)

    def test_intersect_horiz(self):
        l1 = line.Line((0, 0), (self.width, self.height))
        l2 = line.Line((0, self.height // 2), (self.width, self.height // 2))
        intersect = l1.intersect_point(l2)
        self.assertEqual(intersect[0], self.width // 2)
        self.assertEqual(intersect[1], self.height // 2)