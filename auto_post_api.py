  
import glob
import os
import sys
import time
from io import open
from instabot import Bot  # noqa: E402
from dotenv import load_dotenv

sys.path.append(os.path.join(sys.path[0], "../../"))
load_dotenv()
username = os.getenv('INSTA_LOGIN')
password = os.getenv('INSTA_PASSWORD')
posted_pic_list = []
try:
    with open("C/images/upload_images.txt", "r", encoding="utf8") as f:
        posted_pic_list = f.read().splitlines()
except Exception:
    posted_pic_list = []

timeout = 24 * 60 * 60  # pics will be posted every 24 hours

bot = Bot()
bot.login(username = username,  
          password = password)

while True:
    folder_path = "C:/images/"
    pics = glob.glob(folder_path + "/*_crop.jpg")
    pics = sorted(pics)
    try:
        for pic in pics:
            if pic in posted_pic_list:
                continue

            pic_name = pic[:-4].split("-")
            pic_name = "-".join(pic_name[1:])

            print("upload: " + pic_name)

            description_file = folder_path + "/" + pic_name + ".txt"

            if os.path.isfile(description_file):
                with open(description_file, "r") as file:
                    caption = file.read()
            else:
                caption = pic_name.replace("-", " ")

            bot.upload_photo(pic, caption=caption)
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
                # snd msg
                break

            if pic not in posted_pic_list:
                posted_pic_list.append(pic)
                with open("C/images/upload_images.txt", "a", encoding="utf8") as f:
                    f.write(pic + "\n")

            time.sleep(timeout)

    except Exception as e:
        print(str(e))
    time.sleep(60)
