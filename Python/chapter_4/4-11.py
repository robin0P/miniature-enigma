pizzas = ['Pepperoni Pizza', 'Cheese Pizza', 'Classic Pizza']
friend_pizzas = pizzas[:]

pizzas.append('Dominos Pizza')
friend_pizzas.append('Pasaport Pizza')

print("\nMy favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
