# Декодируем QR-код с помощью Python

# Для декодирования QR-кодов с помощью Python вам необходимо установить две
# библиотеки Python в вашей среде Python;
# pip install pyzbar
# pip install pillow

from pyzbar.pyzbar import \
    decode  # Импортируем библиотеку для декодирования QR-кодов
from PIL import Image  # Импортируем библиотеку для работы с изображениями

decocdeQR = decode(Image.open('instagram.png'))  # Открываем изображение
print(decocdeQR[0].data.decode('ascii'))  # Выводим данные изображения
