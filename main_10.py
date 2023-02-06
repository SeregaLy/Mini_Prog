# Подсчитайте количество слов в столбце с помощью Python
# Большинство специалистов по науке о данных используют библиотеку pandas для
# обработки и подготовки данных. В библиотеке pandas нет метода подсчета
# количества слов в тексте. Один из способов решить эту проблему — найти
# длину текста путем разбиения всего текста.

import pandas as pd

data = pd.read_csv(
    "fail.csv", # указать путь до файла
    encoding='utf-8')
print(data.head())

data["Number of Words"] = data["Article"].apply(lambda n: len(n.split()))
print(data.head())
