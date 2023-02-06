#Парсинг профиля GitHub с помощью Python
#Когда мы открываем любую учетную запись GitHub, мы видим изображение профиля,
# имя пользователя и краткое описание пользователя в разделе профиля. Здесь вы
# узнаете, как спарсить изображение профиля GitHub. Для этой задачи вам
# потребуются некоторые знания HTML, запросов и библиотек BeautifulSoup в
# Python.
#         pip install beautifulsoup4


import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/amankharwal"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
print(profile_picture)