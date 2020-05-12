import requests
import os
from PIL import Image


def resize_aspect_fit():
    path = './images/'
    folder = os.listdir(path)
    final_size = 1080;
    for file_name in folder:
        if os.path.isfile(path+file_name):
            image = Image.open(path+file_name)
            file, file_extension = os.path.splitext(path+file_name)
            size = image.size
            ratio = float(final_size) / max(size)
            new_image_size = tuple([int(x*ratio) for x in size])
            image = image.resize(new_image_size, Image.ANTIALIAS)
            new_image = Image.new("RGB", (final_size, final_size))
            new_image.paste(image, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
            file_new_name = f'{file}_resize{file_extension}'
            new_image.paste(image, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
        return new_image
