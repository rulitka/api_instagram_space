# Приложения для загрузки в Instagram фотографий космоса
![Build Status](http://imgsrc.hubblesite.org/hvi/uploads/image_file/image_attachment/29433/2560x1024_wallpaper.jpg)

Размещение в инстаграме фотографий запуской spacex и hubble. Для разсещения используются данные api-приложений:API SpaceX и API Hubble.
В проекте находятся три файла, каждый из которых выполняет свою функцию. 
1) fetch_spacex.py  - делает запрос к API SpaceX и получает фотографии с последнего запуска.
2) fetch_hubble.py - делает запрос к API Hubble и получает фотографии из коллекций, одну из которых нужно выбрать при запуске скрипта. Вот несколько из них: "holiday_cards", "wallpaper", "spacecraft", "news", "printshop", "stsci_gallery". 
3) auto_post_api.py - отвечает за публикацию фотографий, загруженных ранее в аккаунт инстаграмм. 

## Инсталляция
Для начала нужно установить Python 3 с официального сайта Python. После этого нужно поочередно запустить файл fetch_spacex.py через коммандную строку, затем, когда в папке Images появятся фотографии, нужно запустить auto_post_api.py, для того, чтобы опубликовать фотографии в аккаунте инстаграм. Точно также нужно поступить с файлом fetch_hubble.py.

Для того, чтобы все заработало, нужно установить все пакеты, представленные в файле requirements.txt.
```
pip install -r requirements.txt
```
Также нужно создать файл .os в котором нужно разместить логин и пароль от аккаунта инстаграмм, в таком виде: 
```
INSTA_LOGIN = логин
INSTA_PASSWORD = пароль
```
## Лицензия
MIT  © [Akash Nimare](http://akashnimare.in)

## Цели проекта
Этот проект был написан в образовательных целях для веб-разработки на сайте [Devman](https://www.dvmn.org).
