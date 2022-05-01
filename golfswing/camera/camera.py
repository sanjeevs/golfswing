import cv2

class Camera:

    # Port is by default 1 since 0 is used by laptop camera.
    def __init__(self, port=1, width=1280, height=800, fps=120):
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

    def take_video(self, fname, time_secs=6):
        writer = cv2.VideoWriter(fname,
                                 cv2.VideoWriter_fourcc(*'mp4v'),
                                 self.fps(), (self.width(), self.height()))

        num_frames = time_secs * self.fps()

        for _ in range(num_frames):
            frame = self.read_frame()
            writer.write(frame)

        writer.release()

    def take_picture(self, fname):
        frame = self.read_frame()
        cv2.imwrite(fname, frame)

    def __del__(self):
        self.cap.release()