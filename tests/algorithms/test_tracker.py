import unittest
import cv2
import numpy as np

from golfswing.graph2d import screen
from golfswing.algorithms import tracker

class TestTracker(unittest.TestCase):
    def setUp(self):
        self.width = 1280
        self.height = 800
        screen.init(width=self.width, height=self.height)

    def test_tracker_init(self):
        t = tracker.Tracker()
        img = np.zeros(shape=(800, 1280, 3), dtype=np.uint8)
        t.add(img, (0,0, 100, 100))
        t.add(img, (200, 200, 100, 100))
        boxes = t.update(img)
        self.assertEqual(len(boxes), 2)