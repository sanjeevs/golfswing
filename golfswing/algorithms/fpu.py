"""
Frame processing unit.
Currently it uses a hints file instead of object detection
"""

from golfswing.algorithms import tracker
from golfswing.graph2d import utils, parallelogram

class Fpu:
    def __init__(self):
        self.tr1 = tracker.Tracker()

    def setup(self, frame, hints):
        led0_box = utils.create_bounding_box(hints["led0"], 10)
        self.tr1.add(frame, led0_box)

        led1_box = utils.create_bounding_box(hints["led1"], 10)
        self.tr1.add(frame, led1_box)

        self.club_points = [hints["led0"][0], hints["led0"][1],
                            hints["led1"][0], hints["led1"][1]]
        self.target_points = hints["init_ball"]
        self.swing_plane = parallelogram.make_parallelogram(hints["swing_plane_pt0"],
                                                            hints["swing_plane_pt1"],
                                                            hints["swing_plane_pt2"])
        return self.make_screen_desc()

    def update(self, frame):
        tracking_pts =  self.tr1.update(frame)
        self.club_points = [tracking_pts[0][0], tracking_pts[0][1], tracking_pts[1][0],
                            tracking_pts[1][1]]
        return self.make_screen_desc()

    def make_screen_desc(self):
        screen_desc = {}
        screen_desc["ClubLine"] = [self.club_points[0], self.club_points[1],
                                   self.club_points[2], self.club_points[3]]
        screen_desc["TargetLine"] = [self.target_points[0], self.target_points[1]]
        screen_desc["SwingPlane"] = [self.swing_plane.vertices[0][0], self.swing_plane.vertices[0][1],
                                     self.swing_plane.vertices[1][0], self.swing_plane.vertices[1][1],
                                     self.swing_plane.vertices[2][0], self.swing_plane.vertices[2][1],
                                     self.swing_plane.vertices[3][0], self.swing_plane.vertices[3][1]]
        return screen_desc