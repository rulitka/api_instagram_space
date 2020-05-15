import requests
import os
from PIL import Image


def resize_aspect_fit():
    path = './images/'
    folder = os.listdir(path)
    final_size = 1080;
    for file_name in folder:
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path):
            image = Image.open(file_path)
            file, file_extension = os.path.splitext(path+file_name)
            size = image.size
            ratio = float(final_size) / max(size)
            width, height = tuple([int(x*ratio) for x in size])
            new_image_size = [width, height]
            image = image.resize(new_image_size, Image.ANTIALIAS)
            new_image = Image.new("RGB", (final_size, final_size))
            new_image.paste(image, ((final_size-width)//2, (final_size-height)//2))
            new_image.save(f'{file_path}_crop.jpg', 'JPEG')
    return new_image
