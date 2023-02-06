# Вы можете использовать любую библиотеку визуализации данных в Python для
# визуализации линейной зависимости. Я предпочитаю использовать plotly, так
# как он обеспечивает интерактивные результаты. Но так как многие программисты
# на Python используют matplotlib для визуализации данных , я покажу вам, как
# визуализировать линейную связь с Python, используя plotly и matplotlib.
# Итак, давайте импортируем набор данных и все необходимые библиотеки Python
# для этой задачи:


import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram.csv",
    encoding='latin1')
data = data.dropna()

figure = px.scatter(data_frame=data,
                    x="Impressions",
                    y="Likes",
                    size="Likes",
                    trendline="ols",
                    title="Relationship Between Likes and Impressions")
figure.show()

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Relationship Bewtween Likes & Impressions")
sns.regplot(x="Impressions", y="Likes", data=data)
plt.show()
