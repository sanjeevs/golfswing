import cv2

class Camera:
    def __init__(self, port, width=1280, height=800, fps=120):
        self.cap = cv2.VideoCapture(port)

        if not self.cap.isOpened():
            raise ValueError(f"Could not open camera at port={port}")

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FPS, fps)

    def width(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    def height(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def fps(self):
        return int(self.cap.get(cv2.CAP_PROP_FPS))

    def read_frame(self):
        """ Read a frame from the camera. """
        ret, frame = self.cap.read()
        if not ret:
            raise IOError("Camera could not capture a frame")
        return frame

    def read_gray_frame(self):
        frame = self.read_frame()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return gray

    def __del__(self):
        self.cap.release()