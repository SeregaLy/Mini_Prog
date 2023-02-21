# прогамка поможет поздравить друга или родственника, даже в самой большой запаре
#
#

import pandas as pd
from datetime import datetime
import smtplib
from email.message import EmailMessage


def send_email(recipient, subject, msg):     # Функция отправки сообщения почты
    GMAIL_ID = 'your_email_here'    # ваш адрес электронной почты
    GMAIL_PWD = 'your_password here'    # ваш пароль
    email = EmailMessage()  # создаем экземпляр класса EmailMessage
    email['Subject'] = subject  # задаем заголовок
    email['From'] = GMAIL_ID    # задаем имя отправителя

    email['To'] = recipient     # задаем получателя
    email.set_content(msg)  # задаем текст сообщения
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail_obj:  # подключаемся к имеющейся почте
        gmail_obj.ehlo()    # проверяем подключение
        gmail_obj.login(GMAIL_ID, GMAIL_PWD)    # авторизуемся
        gmail_obj.send_message(email)    # отправляем сообщение
    print('Email sent to' + str(recipient) + 'with Subject: \'' + str(
        subject) + '\' and Message: \''' + str(msg) + ' / '')    # выводим сообщение об успешной отправке


def send_bday_emails(bday_file):    # вызываем функцию отправки сообщений
    bdays_df = pd.read_excel(bday_file) # загружаем даты рождения в таблицу
    today = datetime.now().strftime('Sm-8d')    # получаем текущую дату в формате строки
    year_now = datetime.now().strftime('gY')    # получаем текущий год в формате строки
    sent_index = [] # индексы отправленных сообщений

    for idx, item in bdays_df.iterrows():    # перебираем все значения из таблицы
        bday = item['Birthday'].to_pydatetime().strftime('%m-%d')    # получаем дату рождения в формате строки
        if (today == bday) and year_now not in str(item['Last Sent']):    # проверяем на совпадение даты рождения и последнего отправленного сообщения
            msg = 'Happy Birthday' + str(item['Name'] + '!!')    # получаем сообщение об успешной отправке
            send_email(item['Email'], 'Happy Birthday', msg)    # отправляем сообщение
            sent_index.append(idx)    # добавляем индекс отправленного сообщения в список
    for idx in sent_index:    # перебираем индексы отправленных сообщений
        bdays_df.loc[bdays_df.index[idx], 'Last Sent'] = str(year_now)    # обновляем последнее отправленное сообщение в таблице

    bdays_df.to_excel(bday_file, index=False)    # записываем обновленную таблицу в файл


if __name__ == '__main__':
    send_bday_emails('bdays.xlsx')