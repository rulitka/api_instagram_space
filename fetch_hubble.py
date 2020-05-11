import requests
from pathlib import Path
import os
from PIL import Image
import resize


def get_collection(collection_name):
    url = f'http://hubblesite.org/api/v3/images/{collection_name}'
    launche_response = requests.get(url)
    launche_response.raise_for_status()
    images_response = launche_response.json()
    image_id = []
    for number in images_response:
        image_id.append(number["id"])
    return image_id


def get_image(image_id):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    launche_response = requests.get(url)
    launche_response.raise_for_status()
    hubble_image = launche_response.json()['image_files'][-1]['file_url']
    return hubble_image


def save_image(hubble_image, image_id):
    full_file_url = f'https:{hubble_image}'
    file_extension = os.path.splitext(full_file_url)[-1]
    image_name = (f'hubble_{image_id}{file_extension}')
    save_dir = Path('./images/')
    save_dir.mkdir(parents=True, exist_ok=True)
    file_path = save_dir / image_name
    response = requests.get(full_file_url, verify=False)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
    new_image = resize.resize_aspect_fit()
    new_image.save(f'{save_dir}/hubble_{image_id}_crop.jpg', 'JPEG')
    file_path.unlink()


def main():
    collection_name = input ("Введите название коллекции:")
    image_id = get_collection(collection_name)
    for image in image_id:
        hubble_image = get_image(image)
        save_image(hubble_image, image)
    

if __name__ == '__main__':
    main()
