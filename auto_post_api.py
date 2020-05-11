import glob
import os
import sys
import time
from io import open
from instabot import Bot  # noqa: E402
from dotenv import load_dotenv

def post_file():
    sys.path.append(os.path.join(sys.path[0], "../../"))
    load_dotenv()
    username = os.getenv('INSTA_LOGIN')
    password = os.getenv('INSTA_PASSWORD')
    posted_pic_list = []
    try:
        with open("./images/upload_images.txt", "r", encoding="utf8") as f:
            posted_pic_list = f.read().splitlines()
    except Exception:
        posted_pic_list = []

    timeout = 24 * 60 * 60  # pics will be posted every 24 hours

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

                pic_name = pic[:-4].split("-")
                pic_name = "-".join(pic_name[1:])

                print("upload: " + pic_name)

                description_file = os.path.join('folder_path', 'pic_name + ".txt"')

                if os.path.isfile(description_file):
                    with open(description_file, "r") as file:
                        caption = file.read()
                else:
                    caption = pic_name.replace("-", " ")

                bot.upload_photo(pic, caption=caption)
                if bot.api.last_response.ok:
                    pass
                else:
                    break

                if pic not in posted_pic_list:
                    posted_pic_list.append(pic)
                    with open("./images/upload_images.txt", "a", encoding="utf8") as f:
                        f.write(pic + "\n")

                time.sleep(timeout)

        except (FileNotFoundError, IOError):
            print("Wrong file or file path")
        time.sleep(60)


def main():
    post_file()


if __name__ == '__main__':
    main()
