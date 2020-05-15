import glob
import os
import sys
import time
from io import open
from instabot import Bot  # noqa: E402
from dotenv import load_dotenv

def post_file(username, password):
    load_dotenv()
    posted_pic_list = []
    try:
        with open("./images/upload_images.txt", "r", encoding="utf8") as f:
            posted_pic_list = f.read().splitlines()
    except Exception:
        posted_pic_list = []

    bot = Bot()
    bot.login(username = username,  
              password = password)

    folder_path = "./images/"
    pics = glob.glob(folder_path + "/*_crop.jpg")
    pics = sorted(pics) 
    for pic in pics:
        try:
            for pic in pics:
                if pic in posted_pic_list:
                    continue

                bot.upload_photo(pic)
                if bot.api.last_response.ok:
                    pass
                else:
                    break

                if pic not in posted_pic_list:
                    posted_pic_list.append(pic)
                    with open("./images/upload_images.txt", "a", encoding="utf8") as f:
                        f.write(pic + "\n")

        except (FileNotFoundError, IOError):
            print("Wrong file or file path")
        time.sleep(60)


def main():
    username = os.getenv('INSTA_LOGIN')
    password = os.getenv('INSTA_PASSWORD')
    post_file(username, password)


if __name__ == '__main__':
    main()
