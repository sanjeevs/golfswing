import unittest
import os

from golfswing.camera import camera
from golfswing.camera import video

class TestVideo(unittest.TestCase):
    def setUp(self):
        self.camera = camera.Camera(1)
        if not os.path.isdir("tmp"):
            os.mkdir("tmp")

        self.fname  = os.path.join("tmp", "test.mp4")
        if os.path.exists(self.fname):
            os.remove(self.fname)


    def test_mp4(self):
        video.capture_mp4(self.fname, self.camera, time_secs=4)
        self.assertTrue(os.path.exists(self.fname))


if __name__ == "__main__":
    unittest.main()