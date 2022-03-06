import unittest
from golfswing.camera import camera
import time


class TestFps(unittest.TestCase):
    def setUp(self):
        self.camera = camera.Camera(1)

    def test_fps(self):
        """
            Capture 1024 frames and measure the time taken.
            I expect that we will get at least 100 fps
        """
        num_frames = 1024
        start = time.time()
        for _ in range(num_frames):
            self.camera.read_frame()
        end = time.time()

        fps = num_frames / (end - start)
        self.assertGreater(fps, self.camera.fps() * 0.75)

if __name__ == "__main__":
    unittest.main()