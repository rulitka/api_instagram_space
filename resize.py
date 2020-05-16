import requests
import os
from PIL import Image


def resize_aspect_fit(file_path):
    final_size = 1080;
    image = Image.open(file_path)
    size = image.size
    ratio = float(final_size) / max(size)
    width, height = tuple([int(x*ratio) for x in size])
    new_image_size = [width, height]
    image = image.resize(new_image_size, Image.ANTIALIAS)
    new_image = Image.new("RGB", (final_size, final_size))
    new_image.paste(image, ((final_size-width)//2, (final_size-height)//2))
    return new_image


def main():
    resize_aspect_fit(image)


if __name__ == '__main__':
    main()
