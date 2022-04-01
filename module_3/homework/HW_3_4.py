# import json
#
# login = ''
# password = ''
# # verification_data = {'login': 111}
# # with open('verification_data.json', 'w') as f:
# #      json.dump(verification_data, f)
#
# def registration(login, password):
#     login = input('Введите логин, который будете использовать: ')
#     password = input('Введите пароль, который будет использоваться для вашего аккаунта: ')
#     with open('verification_data.json', 'r') as f:
#         verification_data = json.load(f)
#     if login not in verification_data.keys():
#         verification_data[login] = password
#         with open('verification_data.json', 'w') as f:
#             json.dump(verification_data, f)
#     else:
#         print('User already exists')
#
# def log_in(login, password):
#     login = input('Введите логин: ')
#     with open('verification_data.json', 'r') as f:
#         verification_data = json.load(f)
#         while login not in verification_data.keys():
#             print('Авторизация не выпонена, такого логина не существует')
#             login = input('Введите логин: ')
#
#     password = input('Введите пароль: ')
#     with open('verification_data.json', 'r') as f:
#         verification_data = json.load(f)
#         if login in verification_data.keys() and verification_data[login] == password:
#             print('Вы авторизированы')
#         elif verification_data[login] != password:
#             print('Введёный пароль не верен')
#
#
# registration(login, password)
# log_in(login, password)