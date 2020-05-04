import requests
import os
from PIL import Image


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    launches_response = requests.get(url)
    launches_response.raise_for_status()
    images_response = launches_response.json()
    images_response_1 = images_response['links']['flickr_images']
    images_path = "/path/"
    if not os.path.exists(images_path):
        os.mkdir(images_path)
    for i, value in enumerate(images_response_1):
        response = requests.get(value)
        response.raise_for_status()
        with open(images_path+"/spacex{0}.jpeg".format(i+1), 'wb') as file: 
            file.write(response.content)
            i += 1
    resize_aspect_fit()


def resize_aspect_fit():
    path = '/path/'
    dirs = os.listdir(path)
    final_size = 1080;
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            size = im.size
            ratio = float(final_size) / max(size)
            new_image_size = tuple([int(x*ratio) for x in size])
            im = im.resize(new_image_size, Image.ANTIALIAS)
            new_im = Image.new("RGB", (final_size, final_size))
            new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
            new_im.save(f + 'resized.jpg', 'JPEG', quality=90)
            os.remove(path+item)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
