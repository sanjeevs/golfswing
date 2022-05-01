import unittest
import numpy as np

from golfswing.graph2d import screen
from golfswing.algorithms import render
from golfswing.graph2d import line_style

class TestRender(unittest.TestCase):
    def setUp(self) -> None:
        self.frame = np.zeros(shape=(800, 1280, 3), dtype=np.uint8)
        self.width = 1280
        self.height = 800
        screen.init(width=self.width, height=self.height)

    def test_util(self):
        l = [0, 1, 2, 3]
        p = [(0, 1), (2, 3)]
        self.assertEqual(render.lst_to_points(l), p)
        self.assertEqual(render.lst_to_points([]), [])

    def test_utils_ex(self):
        with self.assertRaises(IndexError):
            render.lst_to_points([0])

    def test_target_line(self):
        screen_desc = {'TargetLine': [10, 10]}
        self.assertTrue(np.count_nonzero(self.frame) == 0)
        render.render(self.frame, screen_desc)
        self.assertTrue(np.count_nonzero(self.frame) > 0)

    def test_club_line(self):
        screen_desc = {'ClubLine': [10, 10, 20, 20]}
        self.assertTrue(np.count_nonzero(self.frame) == 0)
        render.render(self.frame, screen_desc)
        self.assertTrue(np.count_nonzero(self.frame) > 0)

    def test_swing_plane(self):
        screen_desc = {'SwingPlane': [10, 10, 10, 20, 20, 10, 20, 20]}
        self.assertTrue(np.count_nonzero(self.frame) == 0)
        render.render(self.frame, screen_desc)
        self.assertTrue(np.count_nonzero(self.frame) > 0)