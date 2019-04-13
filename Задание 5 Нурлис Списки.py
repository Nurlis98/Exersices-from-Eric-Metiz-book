countries = ['Сингапур','Франция','США','Испания','Нидерланды',]

print("Оригинальный список:")
print(countries)

print("\nOтсортированный список в алфавитном порядке:")
print(sorted(countries))

print("\nCнова оригинальный список:")
print(countries)

print("\nВременно отсортированный список в обратном порядке:")
a = sorted(countries, reverse = True)
print(a)

print("\nCнова оригинальный список:")
print(countries)

print("\nОтсортированный список:")
countries.reverse()
print(countries)

print("\nСписок вернулся к исходному порядку:")
countries.reverse()
print(countries)

print("\nОтсортированный список:")
countries.sort()
print(countries)

print("\nОтсортированный список в обратном алфавитном порядке:")
countries.sort(reverse=True)
print(countries)








