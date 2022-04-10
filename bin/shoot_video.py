import os
import sys
import cv2
import json

mypkgdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(mypkgdir)

from golfswing.camera import camera

camera = camera.Camera(0)

print("Waiting to start video")
cv2.waitKey(0)

camera.take_video("temp.mp4", camera)

del camera