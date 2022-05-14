# GolfSwing Project
Use OpenCV to analyze a person's golf swing. This will help detect common mistakes and improve the swing of a high handicap golf player. 

## Solid Iron Contact
It is known that for getting a solid contact with iron, 2 things are required.
* Move the club shaft in the correct plane. The correct plane has been described as having the extended club shaft line always intersecting the target line. The target line is described as a line extending from the ball to the target.

* Club head is square at the point of contact. If it is not then it will result in either a slice or a hook.


## Hardware

### Camera
Using Arducam 1MP Monochrome (black & white) camera at 120fps camera to capture the swing.
It is available on [amazon](https://www.amazon.com/gp/product/B096M5DKY6)

Setting it for 1280x800 with 120 fps and connected to Windows 11 Home edition laptop.


| Camera Specs     | Value                        |
|------------------|------------------------------|
| Sensor           | Monochrome OV9281            |
| Resolution       | 1MP 1280H x 800V             |
| Pixel Size       | 3um x 3um                    |
| Dynamic Range    | 68DB                         |
| Frame Rate       | MJPG 120fps @ 1280x800       |
| IR Sensitivity   | No IR Filter Sensitive to IR |
| Field of view(FOV) | 70 degrees(H)                |


## Links

For getting started check [setup](docs/setup.md)