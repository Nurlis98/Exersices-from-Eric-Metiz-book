prompt = "\nВведите дополнительные ингредиенты для вашей пиццы:"
prompt += "\nПо зaвершению ввведите'quit' "
message = ""
while message != 'quit':
    message = input(prompt+'включен в вашу пиццу')
    if(message != 'quit'):
        print(message)