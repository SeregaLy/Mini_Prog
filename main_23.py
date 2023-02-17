# Парсим таблицу с веб-сайта с помощью Python

# Для очистки таблицы с веб-сайта я буду использовать модуль urllib в Python,
# который уже доступен в стандартной библиотеке Python. Таким образом, вам не
# нужно устанавливать какую-либо внешнюю библиотеку для сбора данных с
# веб-сайта. Ниже показано, как вы можете использовать модуль urlib для
# очистки таблицы с веб-сайта с помощью языка программирования Python:

import urllib.request
import pandas as pd

url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"

with urllib.request.urlopen(url) as i:
    html = i.read()

data = pd.read_htm
