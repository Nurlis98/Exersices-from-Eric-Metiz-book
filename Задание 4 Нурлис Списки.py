guests = ['Роза','Калмамат', 'Нурзат',]
print(guests)
print(guests[0]+' Я приглашаю вас на обед')
print(guests[1]+' Я приглашаю вас на обед')
print(guests[2]+' Я приглашаю вас на обед')

print('\nГость '+guests[0]+' прийти не сможет')
del guests[0]
print(guests)
guests.append('Сыймык')
print(guests)


print("\nРасширение гостей")

guests.insert(0,"Абдылда")
print(guests[0]+' Я приглашаю вас на обед')
print(guests)
guests.insert(3,"Сайпидин")
print(guests[3]+' Я приглашаю вас на обед')
print(guests)
guests.insert(5,"Акжол")
print(guests[5]+' Я приглашаю вас на обед')
print(guests)

print('\nК сожалению могут прийти только два гостя!')
popped_guests: str = guests.pop()
print(guests)
print(popped_guests)
popped_guests: str = guests.pop()
print(guests)
print(popped_guests+' Я сожалею об отмене приглашения.')
popped_guests: str = guests.pop()
print(guests)
print(popped_guests+' Я сожалею об отмене приглашения.')
popped_guests: str = guests.pop()
print(guests)
print(popped_guests+' Я сожалею об отмене приглашения.')
print(guests)
print(guests[0]+' предложение в силе,жду вас на обед')
print(guests[1]+' предложение в силе,жду вас на обед')
del guests[0]
print(guests)
del guests[0]
print(guests)














