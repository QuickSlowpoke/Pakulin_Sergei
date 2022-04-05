
def max_konkoten(list):
    x = ''.join(list)
    x = sorted(x, reverse=True)
    print(x)
    x1 = ''.join(x)
    return print(x1)

listAns = list(input('Введите число или числа через пробел, из них будет собрано максимальное значение: '))

max_konkoten(listAns)
