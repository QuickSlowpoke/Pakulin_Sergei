print('Сейчас вам будет предложено ввести значения 2х точек ладьи\n'
      'В первом варианте вы вводите искомую точку, где ладья стоит\n'
      'А во втором случае где она будет стоять, ответом послужит то,\n'
      'Добирается ли ладья до второй точки за 1 ход, значения могут быть только от 1 до 8 ')


#Проверка на верный ввод значений от 1 до 8, но код естественно не оптимален
while True:
    firstColumn = int(input('Введите номер первой точки по столбцу: '))
    if (firstColumn <= 8) & (firstColumn > 0):
        break
    else:
        print('Напоминаю, вводить значение нужно от 1 до 8, попробуйте ещё раз')

while True:
    firstLine = int(input('Введите номер первой точки по строке: '))
    if (firstLine <= 8) & (firstLine > 0):
        break
    else:
        print('Напоминаю, вводить значение нужно от 1 до 8, попробуйте ещё раз')

while True:
    secondColumn = int(input('Введите номер второй точки по столбцу: '))
    if (secondColumn <= 8) & (secondColumn > 0):
        break
    else:
        print('Напоминаю, вводить значение нужно от 1 до 8, попробуйте ещё раз')

while True:
    secondLine = int(input('Введите номер второй точки по строке: '))
    if (secondLine <= 8) & (secondLine > 0):
        break
    else:
        print('Напоминаю, вводить значение нужно от 1 до 8, попробуйте ещё раз')

#Проверка закончена

if (firstColumn == secondColumn) | (firstLine == secondLine):
    print('YES')
else:
    print('NO')