longMKAD = 109
speed = int(input("Протяжённость МКАД 109 км \nВведите с какой скоростью едет Василий: "))
time = int(input('А сколько он будет ехать часов? Напишите, пожалуйста: '))

result = speed * time % longMKAD
print(f'По итогу он будет на {result}-ом киллометре МКАДа')