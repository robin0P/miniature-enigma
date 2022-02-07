names = ['juliet', 'troy', 'bless']
print("Hey " + names[0].title() + ", would you like to have a dinner with me ? :)")
print("Hey " + names[1].title() + ", would you like to have a dinner with me ? :)")
print("Hey " + names[2].title() + ", would you like to have a dinner with me ? :)")
print(str(len(names)) + " people invited.\n")

print(names[2].title() + " is not going to be in dinner, because he is to busy, instead Denix will come over")
names[2] = "denix"

print("\nHey " + names[0].title() + ", would you like to have a dinner with me ? :)")
print("Hey " + names[1].title() + ", would you like to have a dinner with me ? :)")
print("Hey " + names[2].title() + ", would you like to have a dinner with me ? :)")
print(str(len(names)) + " people invited.\n")
print("Hey people, we found a bigger dinner table!\n")

names.insert(0, "ahmet")
names.insert(1, "elif su")
names.append('kaan')

print("Hey " + names[0].title() + " welcome our dinner table, would you like to have a dinner with me ? :)")
print("Hey " + names[1].title() + " welcome our dinner table, would you like to have a dinner with me ? :)")
print("Hey " + names[2].title() + ", would you like to have a dinner with me ? :)")
print("Hey " + names[3].title() + ", would you like to have a dinner with me ? :)")
print("Hey " + names[4].title() + ", would you like to have a dinner with me ? :)")
print("Hey " + names[5].title() + " welcome our dinner table, would you like to have a dinner with me ? :)")
print(str(len(names)) + " people invited.\n")

print("I can invite only two people for dinner.\n")

popped_1 = names.pop()
print("I'm sorry " + popped_1.title() + " i can't invite you to the dinner.")

popped_2 = names.pop()
print("I'm sorry " + popped_2.title() + " i can't invite you to the dinner.")

popped_3 = names.pop()
print("I'm sorry " + popped_3.title() + " i can't invite you to the dinner.")

popped_4 = names.pop()
print("I'm sorry " + popped_4.title() + " i can't invite you to the dinner.\n")

print("Hey " + names[0].title() + ", you're still invited!")
print("Hey " + names[1].title() + ", you're still invited!")
print(str(len(names)) + " people invited.")

del names[0]
del names[0]

print("\n" + str(names))
