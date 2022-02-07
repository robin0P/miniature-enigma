# Author: Robin Stardust
# Date: 05-02-2022 07:30 A.M.

food = 'Pizza'
print('food == ' + food)
print("\nString tests starting!")

print("food == 'Pizza'")
print(food == 'Pizza')

print("\nfood != 'Pizza'")
print(food != 'Pizza')

print("\nfood.lower() == 'pizza'")
print(food.lower() == 'pizza')

print("\nNumerical tests starting!")
number = 45
print("number = " + str(number))

print("\nnumber == 45")
print(number == 45)

print("\nnumber != 45")
print(number != 45)

print("\nnumber <= 50")
print(number <= 50)

print("\nnumber >= 50")
print(number >= 50)

print("\nLogical tests are starting! (and/or)")

print("\n(number == 45) and (number <= 50)")
print((number == 45) and (number <= 50))

print("\n(number != 45) or (number == 45)")
print((number != 45) or (number == 45))

print("\nList tests are starting! (not in/ in)")
even_numbers = list(range(2,11,2))
print("List is: " + str(even_numbers))

print("\n6 in even_numbers")
print(6 in even_numbers)

print("\n5 not in even_numbers")
print(5 not in even_numbers)

