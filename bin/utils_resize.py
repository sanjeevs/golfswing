import cv2
import sys
from os import listdir
from os.path import isfile, join

def read_image(fname, scale):
    """
    Reads a image from a file.
    :param fname: Image file
    :param scale: Scale the image by percentage
    :return: Image
    """
    img = cv2.imread(fname)
    if img is None:
        raise FileNotFoundError(f"Could not find {fname}")
    if scale < 100:
        width = int(img.shape[1] * scale / 100)
        height = int(img.shape[0] * scale / 100)
        dim = (width, height)
        # resize image
        resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    else:
        resized_img = img
    return resized_img

def main():
    img_dir = "../images/wei_swing_frames/"
    files = [f for f in listdir(img_dir) if isfile(join(img_dir, f))]
    for f in files:
        img = read_image(join(img_dir, f), 60)
        print(f"New frame size if {img.shape[1]} and {img.shape[0]}")
        cv2.imwrite(f, img)

if __name__ == "__main__":
    main()
