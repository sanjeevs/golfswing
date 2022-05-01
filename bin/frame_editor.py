import copy
import os
import sys
import json
import cv2
import argparse
import numpy as np

mypkgdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(mypkgdir)
from golfswing.ui import text

"""
Shoot video for prototype.
"""

# Global Variable to take of point selection
hints =  {}
def init_hints():
    global hints
    hints["target_line"] = [None]
    hints["club_shaft"] = [None] * 2
    hints["club_head"] = [None] * 2
    hints["swing_plane"] = [None] * 2

class KeyState:
    def __init__(self):
        self.name = "TargetState"

    def update(self, key_pressed):
        if key_pressed == ord('q'):
            self.name = "QuitState"
        elif key_pressed == ord('t'):
            self.name = "TargetState"
        elif key_pressed == ord('p'):
            self.name = "SwingPlaneState"
        elif key_pressed == ord('s'):
            self.name = "ClubShaftState"
        elif key_pressed == ord('h'):
            self.name = "ClubHeadState"

state = KeyState()

# Mouse selecting points
def mouse_event_handler(event, x, y, flags, param):
    global hints
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"EventHandler:State={state.name}, ({x}, {y})")
        if state.name == "TargetState":
            hints["target_line"] = (x, y)
        elif state.name == "ClubShaftState":
            if hints["club_shaft"][0] == None:
                hints["club_shaft"][0] = (x, y)
            else:
                hints["club_shaft"][1] = (x, y)
        elif state.name == "ClubHeadState":
            if hints["club_head"][0] == None:
                hints["club_head"][0] = (x, y)
            else:
                hints["club_head"][1] = (x, y)
        elif state.name == "SwingPlaneState":
            if hints["swing_plane"][0] == None:
                hints["swing_plane"][0] = (x, y)
            else:
                hints["swing_plane"][1] = (x, y)

cv2.namedWindow(winname='default')
cv2.setMouseCallback('default', mouse_event_handler)

# Command line processing
parser = argparse.ArgumentParser()

parser.add_argument('--fname', '-f', type=str, required=True, help="Name of the frame")
parser.add_argument('--scale', '-s', type=int, default=100, help="Scaling factor")
args = parser.parse_args()

img = cv2.imread(args.fname)
if args.scale < 100:
    width = int(img.shape[1] * args.scale / 100)
    height = int(img.shape[0] * args.scale / 100)
    dim = (width, height)
    # resize image
    resize = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
else:
    resize = img

while True:
    frame = copy.deepcopy(resize)
    text.fprint(frame, f'{state.name}, p-plane, s-shaft, h-head, t-target')
    cv2.imshow("default", frame)
    key_pressed = cv2.waitKey(0) & 0xFF
    state.update(key_pressed)
    if state.name == "QuitState":
        break
