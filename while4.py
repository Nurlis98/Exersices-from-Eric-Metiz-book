prompt = "\nВведите дополнительные ингредиенты для вашей пиццы:"
prompt += "\nПо зaвершению введите'quit' "
message = " "
while message != 'quit':
    message = input(prompt)
    print(prompt)
    if(message != 'quit'):
        print(message+'добавлен в вашу пиццу')