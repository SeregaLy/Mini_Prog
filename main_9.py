# Время выполнения программы Python
# Итак, чтобы рассчитать время выполнения программы Python, нам нужно выполнить шаги, указанные ниже:

# Во-первых, сохраните время запуска программы в переменную;
# Напишите программу на Python;
# Сохраните время окончания программы в переменной;
# Вычесть время начала программы из времени окончания программы;
# В итоге вы получите время выполнения вашей программы в секундах.


from time import time
start = time()

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Время выполнения: ", execution_time)