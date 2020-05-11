import requests
from pathlib import Path
import os
from PIL import Image
import resize1

def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    launches_response = requests.get(url)
    launches_response.raise_for_status()
    images_response = launches_response.json()
    images_link_list = images_response['links']['flickr_images']
    return images_link_list
    

def save_images(images_link_list):
    for i, value in enumerate(images_link_list):
        save_dir = Path('./images/')
        save_dir.mkdir(parents=True, exist_ok=True)
        image_url = Path(value)
        file_path = save_dir / f'spacex_{image_url.parts[-2]}_{image_url.name}'
        response = requests.get(value)
        response.raise_for_status()
        with open(f'{file_path}', 'wb') as file: 
            file.write(response.content)
        crop_image = resize1.resize_aspect_fit()
        crop_image.save(f'{save_dir}/{file_path.stem}_crop.jpg', 'JPEG')
        file_path.unlink()


def main():
    images_link_list = fetch_spacex_last_launch()
    save_images(images_link_list)

if __name__ == '__main__':
    main()
