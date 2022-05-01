import unittest
import numpy as np

from golfswing.graph2d import screen, line, draw

class TestDraw(unittest.TestCase):
    def setUp(self):
        self.width = 10
        self.height = 10
        screen.init(width=self.width, height=self.height)
        self.img = np.zeros(shape=(screen.WIDTH, screen.HEIGHT, 3), dtype=np.uint8)

    def test_join(self):
        color = (1, 2, 3)
        draw.join(self.img, points=[(0,0), (self.width, self.height)],color=color)
        self.assertEqual(self.img[0][0][0], 1)
        self.assertEqual(self.img[0][0][1], 2)
        self.assertEqual(self.img[0][0][2], 3)

    def test_line_from(self):
        color = (1, 2, 3)
        l1 = line.Line((0,0), (self.width, self.height))
        draw.line_from(self.img, l1, 0, 5)
