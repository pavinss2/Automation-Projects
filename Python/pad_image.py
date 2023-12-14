# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

from PIL import Image, ImageOps
size = (6000, 6000)
with Image.open("Test_Pin.jpg") as im:
    ImageOps.pad(im, size, color="#FFFFFF").save("imageops_pad.png")
