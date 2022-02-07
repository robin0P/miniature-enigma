# Author: Robin Stardust
# Date: 04-02-2022 05:33 P.M.

colleges = ['harvard', 'princeton']
print(colleges)

message =  "I want to go " + colleges[0].title() + "."
print(message)

colleges.append('oxford')
message_2 = colleges[2].title() + " is also good."
print("\n" + str(colleges))
print(message_2)

colleges.insert(2, 'cambridge')
print('\n' + str(colleges))
message_3 = "Newton is graduated from " + colleges[2].title() + " in 1665."
print(message_3)

del colleges[3]
print('\n' + str(colleges))
print("I just changed my mind, i don't want to go Oxford, my goal is toward to the Harvard!")

popped_1 = colleges.pop()
print('\n' + str(colleges))
print("I said i want to go Harvard, not " + popped_1.title())


too_spiky = 'princeton'
colleges.remove(too_spiky)
print('\n' + str(colleges))
print("I know, i'm stubborn right?")

colleges.append('yale')
colleges.append('columbia')
colleges.append('cornell')
colleges.append('brown')
colleges.append('princeton')
colleges.append('dartmouth')
colleges.append('penn')

colleges.sort()
print('\n' + str(colleges))
print("And that's the sorted version of Ivy League")

colleges.sort(reverse = True)
print('\n' + str(colleges))
print("And that's the reverse sorted version of it")

print('\n' + str(sorted(colleges)))
print("This is temporarily sorted version of it")

print('\n' + str(sorted(colleges, reverse = True)))
print("This is temporarily sorted and reversed version of Ivy Leagues")

print("\nThere is totally " + str(len(colleges)) + " Ivy School on the platform.")
