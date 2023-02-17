# QR-код с использованием Python
#  B виртуальной среде Python установим модули PyQRCode и pypng


import pyqrcode   # Импортируем модуль для работы с QR-кодами
import png        # Импортируем модуль для работы с PNG-файлами

link = "https://www.instagram.com/the.clever.programmer/"   # Ссылка на программу
qr_code = pyqrcode.create(link) # Создаем QR-код
qr_code.png("instagram.png", scale=5)   # Сохраняем код в PNG-файл
