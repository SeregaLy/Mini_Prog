#Программа выводит первые n чисел Фибоначчи не считая 0

def fibonachi_nums(num):
    fibonachi = [0, 1]
    for i in range(num - 1):
        fibonachi.append(sum(fibonachi[-2:]))
    return fibonachi

num = int(input())
print(*fibonachi_nums(num))

