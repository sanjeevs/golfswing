#
# Split a video file into frames from a starting frame idx to ending idx.
#

import os
import sys
import argparse
import cv2
from pathlib import Path

mypkgdir = os.path.join(os.path.dirname(__file__), "../..")
sys.path.append(mypkgdir)

from golfswing.camera import video
from golfswing.algorithms import fpu, render
from golfswing.ui import text

# Command line processing
parser = argparse.ArgumentParser()
parser.add_argument('--fname', '-f', type=str, required=True, help="Name of the video file")
parser.add_argument('--out', '-o', type=str, help="Output directory name", default = ".")
parser.add_argument('--prefix', '-p', type=str, help="Output file prefix", default='frame_')
parser.add_argument('--start', '-s', type=int, help="starting frame number", default=0)
parser.add_argument('--end', '-e', type=int, help="ending frame number", default=-1)

args = parser.parse_args()

vid = video.Video(args.fname)
if args.end == -1:
    args.end = vid.num_frames()

# Create the output directory with the same name as fname.
out_dir = Path(args.fname).stem
if not os.path.exists(out_dir):
    print(f">>Creating new {out_dir} for storing all the frames\n")
    os.makedirs(out_dir)

num_digits = len(str(args.end - args.start + 1))
fname_prefix = os.path.join(out_dir, args.prefix)
fname_suffix = str(0).zfill(num_digits)
fname = fname_prefix + fname_suffix + ".png"

print(f"Split {args.fname} from frame {args.start} to {args.end} as {fname}")
for idx, frame in enumerate(vid):
    if idx >= args.start and idx <= args.end:
        fname = fname_prefix + str(idx).zfill(num_digits) + ".png"
        cv2.imwrite(fname, frame)

del vid
cv2.destroyAllWindows()
