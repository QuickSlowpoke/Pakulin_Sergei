firstNumber = int(input('Введите первое число: '))
secondNumber = int(input('Введите второе число: '))
thirdNumber = int(input('Введите третье число: '))

if (firstNumber == secondNumber) & (secondNumber == thirdNumber):
    print(3)
elif (firstNumber == secondNumber) | (firstNumber == thirdNumber) | (secondNumber == thirdNumber):
    print(2)
else:
    print(0)