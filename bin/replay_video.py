import os
import sys
import cv2
import argparse
import json


mypkgdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(mypkgdir)

from golfswing.camera import video
from golfswing.algorithms import fpu, render
from golfswing.ui import text

# Command line processing
parser = argparse.ArgumentParser()
parser.add_argument('--name', '-n', type=str, required=True, help="Name of the scenario")
args = parser.parse_args()

video_fname = args.name + ".mp4"
hints_fname = args.name + ".hints"

with open(hints_fname) as fh:
    hints = json.load(fh)
print(hints)

vid = video.Video(video_fname)
fpu1 = fpu.Fpu()

# Open json file for debug
screen_json = args.name + ".json"
json_fh = open(screen_json, "w")

for idx, frame in enumerate(vid):
    text.fprint(frame, f"Frame {idx}")
    if idx == 0:
        screen_desc = fpu1.setup(frame, hints)
    else:
        screen_desc = fpu1.update(frame)
    screen_desc['frame_idx'] = idx

    json.dump(screen_desc, json_fh)

    render.render(frame, screen_desc)
    cv2.imshow("default", frame)
    key_pressed = cv2.waitKey(1) & 0xff

    if key_pressed == ord('s'):
        text.fprint(frame, f"Frame {idx} Stop")
        cv2.imshow("default", frame)
        key_pressed = cv2.waitKey(0) & 0xff

    if key_pressed == ord('n'):
        text.fprint(frame, f"Frame {idx} Stop")
        cv2.imshow("default", frame)
        key_pressed = cv2.waitKey(0) & 0xff

    if key_pressed == ord('q'):
        break

json_fh.close()
del vid
cv2.destroyAllWindows()
