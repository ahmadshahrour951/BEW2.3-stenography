"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    # /Lessons/Steganography
    - Lesson Plan: https://make-school-courses.github.io/BEW-2.3-Web-Security/
Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""

from PIL import Image
from PIL import ImageDraw, ImageFont
from PIL.ImagePalette import raw


def decode_image(path_to_png):
    """
    Decode image from path
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    for x in range(x_size):
        for y in range(y_size):
            buffer = red_channel.getpixel((x, y))

            binary = bin(buffer)
            lsb = binary[len(binary) - 1]
            lsb = int(lsb)

            rbg = (255, 255, 255) if lsb == 0 else (0, 0, 0)

            decoded_image.putpixel((x, y), rbg)

    decoded_image.save("decoded_image.png")


def encode_image(path_to_png, secret_message):
    """
    Encode secret text to image from path
    """
