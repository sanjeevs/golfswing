import cv2

class Tracker:
    # OpenCV object tracker implementations
    OPENCV_OBJECT_TRACKERS = {
        "csrt": cv2.legacy.TrackerCSRT_create,
        "kcf": cv2.legacy.TrackerKCF_create,
        "boosting": cv2.legacy.TrackerBoosting_create,
        "mil": cv2.legacy.TrackerMIL_create,
        "tld": cv2.legacy.TrackerTLD_create,
        "medianflow": cv2.legacy.TrackerMedianFlow_create,
        "mosse": cv2.legacy.TrackerMOSSE_create
    }

    def __init__(self, algo="mil"):
        if algo not in Tracker.OPENCV_OBJECT_TRACKERS:
            raise ValueError(f"Invalid value of tracker algo {algo}")
        self.algo = algo
        self.trackers = cv2.legacy.MultiTracker_create()

    def add(self, frame, box):
        tracker = Tracker.OPENCV_OBJECT_TRACKERS[self.algo]()
        self.trackers.add(tracker, frame, box)

    def update(self, frame):
        ok, boxes = self.trackers.update(frame)
        if ok:
            result = []
            for box in boxes:
                (x, y, w, h) = [int(v) for v in box]
                center_x = (x + x + w) // 2
                center_y = (y + y + h) // 2
                result.append((center_x, center_y))
            return result
        else:
            return []
