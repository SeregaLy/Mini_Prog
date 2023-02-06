# Чтобы создать систему аутентификации по паролю с помощью Python, вы должны
# выполнить шаги, указанные ниже:

# Создайте словарь имен пользователей с их паролями.
# Затем вы должны запросить пользовательский ввод в качестве имени
# пользователя, используя функцию ввода в Python.
# Затем вам нужно использовать модуль getpass в Python, чтобы запросить
# ввод пользователя в качестве пароля. Здесь мы используем модуль getpass
# вместо функции ввода, чтобы убедиться, что пользователь не видит, что он
# пишет в поле пароля.

import getpass
database = {"aman.kharwal": "123456", "kharwal.aman": "654321"}
username = input("Введите ваше имя пользователя: ")
password = getpass.getpass("Введите ваш пароль : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Введите пароль еще раз: ")
        break
print("Проверено")