age = 'Введите ваш возраст:'
while True:
    age_1 = input(age)
    print(age_1)
    if (age_1) >= str(3):
       print('Вход бесплатный!')
    elif (age_1) <= str(12):
       print('Цена билета 10$')
    else:
       print('Цена билета 15$')



