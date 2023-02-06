# Правильное написание с помощью Python
# Модуль проверки орфографии в Python — один из самых удобных инструментов,
# который можно использовать для исправления слов с ошибками в фрагменте текста.
# Если вы никогда раньше не использовали этот модуль Python, вы можете легко
# установить его в виртуальной среде Python, выполнив указанную ниже команду в
# командной строке или терминале:

from spellchecker import SpellChecker

corrector = SpellChecker()

word = input("Введите слово : ")
if word in corrector:
    print("Правильно")
else:
    correct_word = corrector.correction(word)
    print("Правильное написание следующее: ", correct_word)
