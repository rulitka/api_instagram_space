import requests
from pathlib import Path
import os
from PIL import Image


def return_of_collection(collection_name):
    curl = f'http://hubblesite.org/api/v3/images/{collection_name}'
    launches_response = requests.get(curl)
    launches_response.raise_for_status()
    images_response = launches_response.json()
    image_id = []
    for i in images_response:
        image_id.append(i["id"])
    return image_id


def return_of_images(image_id):
    URL = f'http://hubblesite.org/api/v3/image/{image_id}'
    launches_response = requests.get(URL)
    launches_response.raise_for_status()
    hubble_image = launches_response.json()['image_files'][-1]['file_url']
    full_file_url = f'https:{hubble_image}'
    file_extension = full_file_url.split('.')[-1]
    image_name = (f'hubble_{image_id}.' + file_extension)
    save_dir = Path('C:/images/')
    save_dir.mkdir(parents=True, exist_ok=True)
    file_path = save_dir / image_name
    response = requests.get(full_file_url, verify=False)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
    new_image = resize_aspect_fit()
    new_image.save(f'{save_dir}/hubble_{image_id}_crop.jpg', 'JPEG')
    file_path.unlink()


def resize_aspect_fit():
    path = 'C:/images/'
    dirs = os.listdir(path)
    final_size = 1080;
    for photo in dirs:
        im = Image.open(path+photo)
        f, e = os.path.splitext(path+photo)
        size = im.size
        ratio = float(final_size) / max(size)
        new_image_size = tuple([int(x*ratio) for x in size])
        im = im.resize(new_image_size, Image.ANTIALIAS)
        new_im = Image.new("RGB", (final_size, final_size))
        new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
    return new_im


def main():
    collection_name = input ("Введите название коллекции:")
    image_id = return_of_collection(collection_name)
    for image in image_id:
        return_of_images(image)


if __name__ == '__main__':
    main()
