## Introduction
I am using conda to manage the virtual env. The list of packages to be installed are kept in environment.yml.

1. If required change the env name by editing environment.yml

2. Create the env.
```
    conda env create -f environment.yml
```

3. Activate the env. (say golfswingv2)
```
    conda activate golfswingv2
```

4. Run generic unit tests.
These tests don't require a camera.
```
    python -m unittest tests.graph2d.test_line
```

## Running unittests
Assuming that the camera is connected, then to run all the unittests

```
    python -m unittest discover
```
## Running scripts

### List Cameras
My laptop has  built in webcam and the usb camera.
```
    cd bin
    python list_all_cameras.py
```

### Picture Capture
The easiest script to run from bin dir is to take a photo.

```
    cd bin
    python take_picture.py
```

### Video Capture
There are 2 scripts. One captures the video in live mode for say 4 seconds and the other
replays the video from the file.

```
    cd bin
    python shoot_video -n test1 -t 4   // Creates test1.mp4 in the current dir
    python replay_video -n test1
```

## Future Work
How to structure the code layout so that unit tests are auto detected?

How to differentiate between unit tests that require resources like camera vs that dont?
