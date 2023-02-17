# Извлечение текста из PDF с помощью Python
# Для этой задачи вам необходимо установить библиотеку Python, известную как
# PyPDF2.

import PyPDF2

pdf = open("Aman.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0) # указываем номер страницы с которой извлекаем текст
print(page.extractText())
