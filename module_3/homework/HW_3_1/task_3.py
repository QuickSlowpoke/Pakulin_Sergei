
num = int(input('Введите число: '))
result = 0

while num != 0:
    num1 = num % 10
    result += num1
    num = num // 10

print(result)