# Групповые анаграммы с использованием Python
# Группировка анаграмм — один из популярных вопросов на собеседованиях по
# программированию. Здесь вам будет дан список слов, и вы должны написать
# алгоритм для группировки всех слов, которые являются анаграммами друг друга.
# Ниже показано, как вы можете написать функцию Python для группировки
# анаграмм:

from collections import defaultdict


def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].app


words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))
