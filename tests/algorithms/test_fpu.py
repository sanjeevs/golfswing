import unittest

import numpy as np

from golfswing.graph2d import screen
from golfswing.algorithms import fpu

class TestFpu(unittest.TestCase):
    def setUp(self) -> None:
        self.frame = np.zeros(shape=(800, 1280, 3), dtype=np.uint8)
        self.width = 1280
        self.height = 800
        screen.init(width=self.width, height=self.height)

    def test_setup(self):
        f1 = fpu.Fpu()

        hints = {}
        hints["led0"] = (100, 200)
        hints["led1"] = (150, 250)
        hints["init_ball"] = (400, 500)
        hints["swing_plane_pt0"] = (20, 30)
        hints["swing_plane_pt1"] = (30, 40)
        hints["swing_plane_pt2"] = (40, 50)

        screen_desc = f1.setup(self.frame, hints)
        self.assertEqual(len(screen_desc.keys()), 3)