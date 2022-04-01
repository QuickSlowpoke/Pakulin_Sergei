# number = 7
# answer = 0
#
# while number != answer:
#     answer = int(input())
#     if number == answer:
#         print('Winner chicken dinner')
#     elif number > answer:
#         print('Need more')
#     else:
#         print('Need less')

# n = 100
#
# for i in range(1, n):
#     c = 0
#     for j in range(2, i):
#         if i % j == 0:
#             c += 1
#     if c == 0:
#         print(i)

# n = 100
# i = 0
#
# while i < n:
#     print(i)
#     i += 1

# data = {'testlog': 'testpassword'}
# secret_info = '43'
#
# while True:
#     q1 = input('Вход или регистрация?')
#     if q1 == 'вход':
#         login = input('Введите логин: ')
#         password = input('Введите пароль: ')
#         if login in data.keys():
#             if data[login] == password:
#                 print('Вход выполнен')
#                 print(secret_info)
#         else:
#             print('Логин не верен')
#     elif q1 == 'регистрация':
#         login = input('Введите логин: ')
#         password = input('Введите пароль: ')
#         if login in data.keys():
#             print('Логин занят')
#         else:
#             data[login] = password
#             print('Регистрация завершена')

l = [1, 2, 3, 4, 1, 4, 5, 6, '111213', '3', '3']
l_unique = []

for i in l:
    if i not in l_unique:
        l_unique.append(i)

print(l_unique)

print(list(set(l)))