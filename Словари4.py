favorite_numbers= {}


favorite_numbers['Python'] = ' - высокоуровневый язык программирования с динамической типизацией.'
favorite_numbers['Переменные'] = " - могут содержать только буквы, числа и нижние подчеркивания."
favorite_numbers['Метод'] = ' - это действие которое может быть применено на различных данных'
favorite_numbers['Словари'] = ' - структуры данных, предназначенные для объединения взаимосвязанной информации'

for name, favorite in favorite_numbers.items():
    print(name.title() +
     favorite.title())


