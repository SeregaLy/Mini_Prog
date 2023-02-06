import random

n = random.randrange(1, 10)
guess = int(input("Введите любое число: "))
while n != guess:
    if guess < n:
        print("Введите число еще раз:")
        guess = int(input("Повторите ввод: "))
    elif guess > n:
        print("Искомое число меньше!")
        guess = int(input("Введите число еще раз: "))
    else:
        break
print("Вы правильно догадались!!")
