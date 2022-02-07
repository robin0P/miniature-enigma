my_foods = ['pizza', 'fries', 'egg']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are here:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are here:")
for food in friend_foods:
    print(food)
