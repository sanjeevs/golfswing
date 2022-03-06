import cv2
from golfswing.camera import camera

def capture_mp4(fname, camera, time_secs):
    writer = cv2.VideoWriter(fname,
                             cv2.VideoWriter_fourcc(*'mp4v'),
                             camera.fps(), (camera.width(), camera.height()))

    num_frames = time_secs * camera.fps()

    for _ in range(num_frames):
        frame = camera.read_frame()
        writer.write(frame)

    writer.release()
