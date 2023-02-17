# Анимированный точечный график с использованием Python
# библиотеку Python plotly можно использовать для создания анимированных
# графиков, поэтому мы можем использовать библиотеку Plotly для визуализации
# диаграммы рассеяния с помощью Python.


import plotly.express as px      # Импортируем библиотеку для визуализации графиков

data = px.data.gapminder()        # Создаем объект данных для визуализации графиков
print(data.head())                # Выводим первые 5 значений данных для визуализации графиков
px.scatter(data, x="gdpPercap", y="lifeExp", animation_frame="year",    # Создаем объект для визуализации графиков
           animation_group="country",
           size="pop", color="country", hover_name="country",
           log_x=True, size_max=55, range_x=[100, 100000], range_y=[25, 90])
