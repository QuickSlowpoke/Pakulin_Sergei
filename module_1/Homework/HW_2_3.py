print('Придумайте, пожалуйста, пароль\n'
      'Он должен состоять из заглавных и прописных латинских букв\n'
      'И иметь длину более 8 символов')
password = input('Придумайте, пожалуйста, пароль: ')

while len(password) < 8 or password.isupper() or password.islower():
        print('Вы ввели не верное значение')
        password = input('Придумайте, пожалуйста, пароль: ')

print('Пароль принят')