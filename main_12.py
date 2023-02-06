# Метод emoji.emojize помогает вам написать описание любого смайлика внутри
# «::» во время написания фрагмента текста. Ниже приведены примеры описаний
# некоторых популярных эмодзи:
#
# :недурно:
# :Красное сердце:
# :улыбающееся лицо:
# Вы можете использовать описание любого смайлика внутри «::», чтобы
# распечатать смайлик с помощью Python. Описание всех эмодзи можно найти
# здесь . https://carpedm20.github.io/emoji/
# Теперь давайте посмотрим на пример того, как печатать смайлики с
# помощью Python:



import emoji

print(emoji.emojize(f"I love reading books :books:"))
print(emoji.emojize(
   "Some people have a very sensitive heart:red_heart:, please be kind with them.:hibiscus:"))
