import unittest
from golfswing.graph2d import screen


class TestScreen(unittest.TestCase):
    def setUp(self):
        self.width = 1280
        self.height = 800
        screen.init(width=self.width, height=self.height)

    def test_x(self):
        self.assertEqual(screen.s2c_x(100), 100)
        self.assertEqual(screen.c2s_x(200), 200)

    def test_s2c_y(self):
        self.assertEqual(screen.s2c_y(0), self.height)
        self.assertEqual(screen.s2c_y(self.height), 0)
        self.assertEqual(screen.s2c_y(10), self.height - 10)

    def test_c2s_y(self):
        self.assertEqual(screen.c2s_y(0), screen.HEIGHT)


if __name__ == "__main__":
    unittest.main()