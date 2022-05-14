import os
import sys
import cv2
import argparse
import json


mypkgdir = os.path.join(os.path.dirname(__file__), "../..")
sys.path.append(mypkgdir)

from golfswing.camera import video
from golfswing.algorithms import fpu, render
from golfswing.ui import text

# Command line processing
parser = argparse.ArgumentParser()
parser.add_argument('--fname', '-f', type=str, required=True, help="Name of the video file")

args = parser.parse_args()

vid = video.Video(args.fname)

for idx, frame in enumerate(vid):
    text.fprint(frame, f"Frame {idx}")
    cv2.imshow("default", frame)
    key_pressed = cv2.waitKey(1) & 0xff

    if key_pressed == ord('s'):
        text.fprint(frame, f"Frame {idx} Stop")
        cv2.imshow("default", frame)
        key_pressed = cv2.waitKey(0) & 0xff
        print(f"Frame stopped at {idx}")

    if key_pressed == ord('q'):
        print(f"Frame quit at {idx}")
        break

del vid
cv2.destroyAllWindows()
