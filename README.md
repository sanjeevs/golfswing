# GolfSwing Project
Use OpenCV to analyze a person's golf swing. This will help detect common mistakes and improve the swing.

## Camera
Using Arducam 1MP Monochrome (black & white) camera at 120fps camera to capture the swing.
It is available on [amazon](https://www.amazon.com/gp/product/B096M5DKY6)

Setting it for 1280x800 with 120 fps and connected to Windows 11 Home edition laptop.

### Tests
tests/camera/test_camera.py : Get a frame from camera
tests/camera/test_fps.py : Test frame rate. Got 113 fps
tests/camera/test_vide.py: Created a mp4 file for 4 secs.