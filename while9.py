sandwich_orders = ['Tuna','Cheese','Pastromi','Panini','Pastromi','with Ham','Pastromi']
finished_sandwiches = []

for finished_sandwiches in sandwich_orders:
    print('I made your '+finished_sandwiches+' sandwich!')


while 'Pastromi' in sandwich_orders:

   sandwich_orders.remove('Pastromi')

print()
print(sandwich_orders)
print('\nPastromi over!')



