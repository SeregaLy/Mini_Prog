# Найти пропущенный номер с помощью Python
# Дан массив, содержащий диапазон чисел от 0 до n с пропущенным числом,
# найдите пропущенное число во входном массиве.

def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output


listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(f"Пропущены следующие числа: {(findMissingNumbers(listOfNumbers))}")
