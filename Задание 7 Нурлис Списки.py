cityes = ['Москва','Лондон', 'Париж',]
print(cityes)

print(cityes[0]+'-столица Российской Федерации, город федерального значения,')
print(cityes[1]+'-столица и крупнейший город Соединённого Королевства Великобритании и Северной Ирландии.')
print(cityes[2]+'-город, столица Франции, административный центр региона Иль-де-Франс.')

del cityes[0]
print(cityes)
cityes.append('Сингапур')
print(cityes[2]+' город-государство, расположенный на островах в Юго-Восточной Азии.')

print(cityes)


cityes.insert(0,"Берлин")
print(cityes[0]+'-столица и крупнейший город Германии')
print(cityes)
cityes.insert(3,"Киев")
print(cityes[3]+'-столица и крупнейший город Украины, Город-Герой.')
print(cityes)
cityes.insert(5,"Будапешт")
print(cityes[5]+'-столица Венгрии, разделенная на две части рекой Дунай. ')
print(cityes)

cityes_guests: str = cityes.pop()
print(cityes)

print("Оригинальный список:")
print(cityes)

print("\nOтсортированный список в алфавитном порядке:")
print(sorted(cityes))

print("\nCнова оригинальный список:")
print(cityes)

print("\nВременно отсортированный список в обратном порядке:")
a = sorted(cityes, reverse = True)
print(a)

print("\nCнова оригинальный список:")
print(cityes)

print("\nОтсортированный список:")
cityes.reverse()
print(cityes)

print("\nСписок вернулся к исходному порядку:")
cityes.reverse()
print(cityes)

print("\nОтсортированный список:")
cityes.sort()
print(cityes)

print("\nОтсортированный список в обратном алфавитном порядке:")
cityes.sort(reverse=True)
print(cityes)

print(len(cityes))












