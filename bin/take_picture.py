import os
import sys
import cv2

mypkgdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(mypkgdir)

from golfswing.camera import camera

camera = camera.Camera(0)
fname = "temp.png"

# font
font = cv2.FONT_HERSHEY_SIMPLEX
thickness = 2
font_scale = 1

while True:
    frame = camera.read_frame()
    img = cv2.putText(frame, 'Frame1: Press s to snap', (10, 30), font,
                      font_scale, (255, 255, 0), thickness, cv2.LINE_AA)
    cv2.imshow("default", img)
    key_pressed = cv2.waitKey(1) & 0xff

    if key_pressed == ord('s'):
        camera.take_picture(fname)
        break
    if key_pressed == ord('q'):
        break

del camera
cv2.destroyAllWindows()