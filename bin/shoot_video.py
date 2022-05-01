import os
import sys
import json
import cv2
import argparse
import numpy as np

mypkgdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(mypkgdir)

from golfswing.camera import camera
from golfswing.ui import key_sm, text
from golfswing.algorithms import fpu, render

"""
Shoot video for prototype.
"""

# Global Variable to take of point selection
target_line_points = [None] * 2
club_line_points = [None] * 4
plane_line_points = [None] * 6
hints = {}
hints["led0"] = (-1, -1)
hints["led1"] = (-1, -1)
hints["init_ball"] = (-1, -1)
hints["swing_plane_pt0"] = (-1, -1)
hints["swing_plane_pt1"] = (-1, -1)
hints["swing_plane_pt2"] = (-1, -1)

state = key_sm.SetupState()

# Mouse selecting points
def mouse_event_handler(event, x, y, flags, param):
    global hints
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"EventHandler:State={state.name}, ({x}, {y})")
        if state.name == "TargetHintState":
            hints["init_ball"] = (x, y)
        elif state.name == "ClubHintState":
            if hints["led0"] == (-1, -1):
                hints["led0"] = (x, y)
            else:
                hints["led1"] = (x, y)
        elif state.name == "PlaneHintState":
            if hints["swing_plane_pt0"] == (-1, -1):
                hints["swing_plane_pt0"] = (x, y)
            elif hints["swing_plane_pt1"] == (-1, -1):
                hints["swing_plane_pt1"] = (x, y)
            else:
                hints["swing_plane_pt2"] = (x, y)


def draw_hints(frame):
    if hints["init_ball"] != (-1, -1):
        cv2.circle(frame, center=hints["init_ball"], radius=5, color=(0,0,255), thickness=-1)

    if hints["led0"] != (-1, -1):
        cv2.circle(frame, center=hints["led0"], radius=5, color=(0, 255, 255), thickness=-1)

    if hints["led1"] != (-1, -1):
        cv2.circle(frame, center=hints["led1"], radius=5, color=(0, 255, 255), thickness=-1)

    if hints["swing_plane_pt0"] != (-1, -1):
        cv2.circle(frame, center=hints["swing_plane_pt0"], radius=5, color=(0, 128, 128), thickness=-1)

    if hints["swing_plane_pt1"] != (-1, -1):
        cv2.circle(frame, center=hints["swing_plane_pt1"], radius=5, color=(0, 128, 128), thickness=-1)

    if hints["swing_plane_pt2"] != (-1, -1):
        cv2.circle(frame, center=hints["swing_plane_pt2"], radius=5, color=(0, 128, 128), thickness=-1)

cv2.namedWindow(winname='default')
cv2.setMouseCallback('default', mouse_event_handler)

# Command line processing
parser = argparse.ArgumentParser()
parser.add_argument('--name', '-n', type=str, required=True, help="Name of the scenario")
parser.add_argument('--time', '-t', type=int, default=6, help="Length of video to save in sec")
parser.add_argument('--camera', '-c', default=0)

args = parser.parse_args()

# Index 0 is usb camera for me and not the laptop camera.
camera = camera.Camera(args.camera)
fpu1 = fpu.Fpu()
is_hints_done = False
frame_idx = 0

while True:
    frame = camera.read_frame()

    text.fprint(frame, f'{state.name} h-Hints [t-Target,c-Club,p-Plane], l-live, s-Save')
    frame_idx +=1

    if state.name == "LiveState":
        if not is_hints_done:
            screen_desc = fpu1.setup(frame, hints)
            is_hints_done = True
        else:
            screen_desc = fpu1.update(frame)

        render.render(frame, screen_desc)
    else:
        draw_hints(frame)
        is_hints_done = False

    cv2.imshow("default", frame)

    key_pressed = cv2.waitKey(1) & 0xff
    next_state = state.update(key_pressed)

    if next_state is not None:
        state = next_state

    if state.name == "QuitState" or state.name == "SaveState":
        break

print(f"Hints={hints}")
hints_file = args.name + ".hints"
with open(hints_file, "w") as fh:
    json.dump(hints, fh)

if state.name == "SaveState":
    black_frame = np.zeros(shape=(camera.height(), camera.width(), 3), dtype=np.uint8)
    video_file = args.name + ".mp4"
    text.fprint(black_frame, f'Recording directly to file {video_file} for {args.time} secs')
    cv2.imshow("default", black_frame)
    key_pressed = cv2.waitKey(1) & 0xff
    camera.take_video(video_file, args.time)

del camera
cv2.destroyAllWindows()