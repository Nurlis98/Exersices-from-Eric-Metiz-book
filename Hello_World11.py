my_foods = ['Four Seasons','Pepperoni','Assorti','Cheese','Margarita']
for pizza in my_foods:
    print(pizza)
    print('I like '+pizza+" pizza!")
print('I really love pizza!')

friend_pizzas= my_foods[:]
print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
friend_pizzas.append('pizza with meat')
print(friend_pizzas)



