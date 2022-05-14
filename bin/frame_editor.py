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
GUI to mark the various points in a image.
The user is expected to click the various points and the output is written
to a json file. 
"""


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

# ------------------------------------------------------------
# Global Variable to take of point selection.
# -----------------------------------------------------------
state = KeyState()
hints = {}

def init_hints():
    global hints
    hints["width"] = 0
    hints["height"] = 0
    hints["target_line"] = [None]
    hints["club_shaft"] = [None] * 2
    hints["swing_plane"] = [None] * 2

def draw_hints(frame):
    for pt in hints["target_line"]:
        if pt is not None:
            cv2.circle(frame, center=pt, radius=5, color=(255, 0, 0), thickness=-1)

    for pt in hints["club_shaft"]:
        if pt is not None:
            cv2.circle(frame, center=pt, radius=5, color=(0, 255, 0), thickness=-1)

    for pt in hints["swing_plane"]:
        if pt is not None:
            cv2.circle(frame, center=pt, radius=5, color=(128, 128, 128), thickness=-1)


# Event handler. Mouse selecting points
#
def mouse_event_handler(event, x, y, flags, frame):
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

        elif state.name == "SwingPlaneState":
            if hints["swing_plane"][0] == None:
                hints["swing_plane"][0] = (x, y)
            else:
                hints["swing_plane"][1] = (x, y)

        draw_hints(frame)
        cv2.imshow("default", frame)

def next_state_s(state_name):
    if state_name == "TargetState":
        return "s-Swing, c-ClubShaft, h-ClubHead, q-Quit"
    elif state_name == "SwingPlaneState":
        return "t-Target, c-ClubShaft, h-ClubHead, q-Quit"
    elif state_name == "ClubShaftState":
        return "t-Target, s-Swing, h-ClubHead, q-Quit"
    elif state_name == "ClubHeadState":
        return "t-Target, s-Swing, c-ClubShaft, q-Quit"
    else:
        return f"OOPS: Invalid decode {state.name}"

def parse_args(argv):
    """
    Command line processing
    :param argv:
    :return: Arguments passed.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('--fname', '-f', type=str, required=True, help="Name of the frame")
    parser.add_argument('--scale', '-s', type=int, default=100, help="Scaling factor")
    parser.add_argument('--out', '-o', type=str, default='out.png', help="create output if scaling is used")
    parser.add_argument('--hint', type=str, help='Hints file for image')
    args = parser.parse_args()

    if args.hint is None:
        args.hint = os.path.splitext(args.fname)[0] + ".hint"

    print(f">> Hints will be written to {args.hint}")
    return args

def read_image(fname, scale):
    """
    Reads a image from a file.
    :param fname: Image file
    :param scale: Scale the image by percentage
    :return: Image
    """
    img = cv2.imread(fname)
    if scale < 100:
        width = int(img.shape[1] * scale / 100)
        height = int(img.shape[0] * scale / 100)
        dim = (width, height)
        # resize image
        resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    else:
        resized_img = img
    return resized_img

def main(argv):
    global hints, frame

    args = parse_args(argv)

    img = read_image(args.fname, args.scale)
    if args.scale < 100:
        print(f">>Creating output scale={args.scale} image as {args.out}")
        cv2.imwrite(args.out, img)

    init_hints()
    hints["width"] = img.shape[1]
    hints["height"] = img.shape[0]

    frame = copy.deepcopy(img)
    cv2.namedWindow(winname='default')
    cv2.setMouseCallback('default', mouse_event_handler, frame)

    while True:
        text.fprint(frame, f'{state.name}, {next_state_s(state.name)}')

        cv2.imshow("default", frame)

        key_pressed = cv2.waitKey(0) & 0xFF
        state.update(key_pressed)
        if state.name == "QuitState":
            break

    json_hints = json.dumps(hints, indent=4)
    with open(args.hint, "w") as fh:
        fh.write(json_hints)

if __name__ == "__main__":
    main(sys.argv)