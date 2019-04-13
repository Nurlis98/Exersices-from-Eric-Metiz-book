responses = {}

# Установка флага продолжения опроса.
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя.
    name = input("\nВведите имя: ")
    response = input("Где вы бы хотели проввести свой отпуск?")

    # Ответ сохраняется в словаре:
    responses[name] = response

    # Проверка продолжения опроса.
    repeat = input("Хотите спросить у других людей?(да/ нет) ")
    if repeat == 'нет':
        polling_active = False

# Опрос завершен, вывести результаты.
print("\n--- Вывод результатов ---")
for name, response in responses.items():
    print(name + " хочет провести свой отпуск в " + response + "е.")

