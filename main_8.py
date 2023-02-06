# Групповые элементы одинаковых индексов с использованием Python
# Чтобы сгруппировать элементы одного и того же индекса, у вас изначально будет
# два или более списков внутри списка, например [[a, b], [c, d]]. Чтобы
# сгруппировать элементы этих списков, вам нужно создать два новых списка, в
# которых вы будете хранить элементы обоих списков с индексом 0 [a, c] и
# индексом 1 [b, d]. В этом смысл группировки элементов одних и тех же
# индексов.


inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
outputLists = []
index = 0

for i in range(len(inputLists[0])):
    outputLists.append([])
    for j in range(len(inputLists)):
        outputLists[index].append(inputLists[j][index])
    index = index + 1
a, b, c = outputLists[0], outputLists[1], outputLists[2]
print(a, b, c)
