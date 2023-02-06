# Визуализация данных о ценах на акции в реальном времени с использованием Python

# Чтобы создать приложение для визуализации данных о ценах на акции в реальном
# времени, я буду использовать библиотеку Streamlit на Python. В этой задаче
# мы можем использовать библиотеку Streamlit для создания интерактивного пользовательского интерфейса, в котором пользователь будет вводить название любой компании, а данные о цене акций будут визуализированы в качестве конечного результата.

# Для задачи визуализации цен на акции мы можем использовать любую библиотеку
# визуализации данных на Python, совместимую с фреймворком Streamlit. Но для
# простоты я буду использовать библиотеку matplotlib в Python. Теперь ниже
# показано, как с помощью Python можно создать приложение для визуализации
# данных о ценах на акции в реальном времени:

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import streamlit as st
import datetime
from datetime import date, timedelta

today = date.today()

d1 = today.strftime("%Y/%m/%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y/%m/%d")
start_date = d2

st.title("Real-time Stock Price Data")
a = st.text_input("Enter Any Company >>:")
data = web.DataReader(name=a, data_source='yahoo', start=start_date,
                      end=end_date)
fig, ax = plt.subplots()
ax = data["Close"].plot(figsize=(12, 8), title=a + " Stock Prices",
                        fontsize=20, label="Close Price")
plt.legend()
plt.grid()
st.pyplot(fig)
