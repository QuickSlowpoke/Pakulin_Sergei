# # Task №1
#
# def area(a, b, c):
#     p = (a + b + c) / 2
#     sq = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     sq = '%.3f'%sq
#     return sq
#
# first = int(input('Введите первую сторону треугольника: '))
# second = int(input('Введите вторую сторону треугольника: '))
# third = int(input('Введите третью сторону треугольника: '))
#
# print(f'Площадь треугольника равна {area(first, second, third)} см')
#
# # Task №2
# import re
#
# def word_length(word):
#     word = re.split('[, \-!?:.-]+', word)
#     for i in word:
#         if len(i) < 5:
#             print(i)
#
#
# s = 'Было просто пасмурно, дуло с севера, ' \
#     'А к обеду насчитал сто градаций серого.' \
#     'Так всегда первого ноль девятого,' \
#     'То ли весь мир сошёл с ума, то ли я - того.' \
#     'На столе записка от неё смятая,' \
#     'Недопитый виски допиваю с матами.' \
#     'Посмотрю в окно, допишу главу,' \
#     'Первое сентября, дворник жжёт листву.' \
#     'И серым облакам наплевать на нас,' \
#     'Если знаешь, как жить - живи' \
#     'Ты хотела плыть, как все?' \
#     'Так плыви!'
#
# word_length(s)

# # Task №3
#
# def max_konkoten(list):
#     x = ''.join(list)
#     x = sorted(x, reverse=True)
#     print(x)
#     x1 = ''.join(x)
#     return print(x1)
#
# listAns = list(input('Введите число, из него будет собрано максимальное значение: '))
#
# max_konkoten(listAns)