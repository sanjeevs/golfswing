import cv2

""" Process video files as an iterator"""

class Video:
    def __init__(self, fname):
        self.cap = cv2.VideoCapture(fname)
        if not self.cap.isOpened():
            raise ValueError(f"Could not open {fname}")

    def __iter__(self):
        return self

    def __next__(self):
        if self.cap.grab():
            flag, frame = self.cap.retrieve()
            if not flag:
                raise StopIteration
            else:
                return frame
        else:
            raise StopIteration

    def __del__(self):
        self.cap.release()

    def num_frames(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
