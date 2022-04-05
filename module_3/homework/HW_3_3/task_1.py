
def area(a, b, c):
    p = (a + b + c) / 2
    sq = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    sq = '%.3f'%sq
    return sq

first = int(input('Введите первую сторону треугольника: '))
second = int(input('Введите вторую сторону треугольника: '))
third = int(input('Введите третью сторону треугольника: '))

print(f'Площадь треугольника равна {area(first, second, third)} см')