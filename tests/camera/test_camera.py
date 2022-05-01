import unittest

import numpy as np

from golfswing.camera import camera
import cv2


class TestCamera(unittest.TestCase):
    def setUp(self):
        self.camera = camera.Camera(1)

    def test_frame(self):
        frame = self.camera.read_frame()
        self.assertTrue(type(frame).__module__ == 'numpy')
        self.assertEqual(frame.dtype, 'uint8')
        self.assertTrue(frame.shape == (self.camera.height(), self.camera.width(), 3))

if __name__ == "__main__":
    unittest.main()