# Task №1
#
# l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']
# counter = {}
#
# for i in l:
#     counter[i] = counter.get(i, 0) + 1
#
# l_repro = {i: count for i, count in counter.items() if count > 1}
#
# print(l_repro)
#
# Task №2

# from random import randint
#
# n = 5
# m = [[randint(0, 100) for i in range(n)] for j in range(n)]
# print(m)

# print(max(m))

# Как будто бы не шибко правильный вариант, но код работает)) Сначала находим массив с максимальными значениями
# а после находим максимальное значение из максимального массива

# l_big = max(m)
# print(max(l_big))

# Task №3
#
# d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
#
# d = dict(zip(d.values(), d.keys()))
# print(d)


