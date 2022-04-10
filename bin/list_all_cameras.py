import cv2

cameras = []

for idx in range(10):
    cap = cv2.VideoCapture(idx)
    if cap.isOpened():
        cameras.append(idx)
        cap.release()

for i in cameras:
    print(f"Camera idx {i} is available")