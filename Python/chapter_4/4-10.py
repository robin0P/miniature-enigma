odd_numbers = [value for value in range(1,21,2)]
for number in odd_numbers:
    print(number)

print("\nThe first three item's in the list are: ")
for number in odd_numbers[0:3]:
    print(number)

print("\nThree items from the middle of the list are: ")
for number in odd_numbers[4:7]:
    print(number)

print("\nThe last three items in the list are: ")
for number in odd_numbers[-3:]:
    print(number)
