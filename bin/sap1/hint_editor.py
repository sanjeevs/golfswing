import argparse
import cv2
import json
import sys
from pathlib import Path


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

def draw_hints(frame):
    for pt in hints["target_line"]:
        if pt is not None:
            print(pt)
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
            hints["target_line"][0] = (x, y)

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


def parse_args(argv):
    """
    Parses the command line arg
    :param argv:
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--fname', '-f', type=str, required=True, help ="png file for frame")
    parser.add_argument('--out', '-o', type=str, help="json file for frame")
    args = parser.parse_args()

    if args.out is None:
        args.out = Path(args.fname).stem + ".json"

    return args

def main(argv):
    global hints

    args = parse_args(argv)
    frame = cv2.imread(args.fname)
    if frame is None:
        print(f"OOPS could not read {args.fname}")
        sys.exit(-1)


    init_hints()
    hints["width"] = frame.shape[1]
    hints["height"] = frame.shape[0]

    cv2.namedWindow(winname='default')
    cv2.setMouseCallback('default', mouse_event_handler, frame)

    while True:
        cv2.imshow('default', frame)
        key_pressed = cv2.waitKey(0) & 0xff
        state.update(key_pressed)
        if state.name == "QuitState":
            break

    json_hints = json.dumps(hints, indent=4)
    with open(hints_fname, "w") as fh:
        fh.write(json_hints)

if __name__ == "__main__":
    main(sys.argv)


