import cv2

# font
font = cv2.FONT_HERSHEY_SIMPLEX
thickness = 2
font_scale = 1

def fprint(frame, msg):
    frame = cv2.putText(frame, msg, (10, 30), font,
                      font_scale, (255, 255, 0), thickness, cv2.LINE_AA)
