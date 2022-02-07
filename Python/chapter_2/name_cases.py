# Name: Robin Stardust
# Date: 04:02:2022 08:52 A.M
# What the program does: Program is just simply storing two string values into two different variables in line 5 and 6 respectively, then concatenating this two values at the line 7 with the space,then it prints the lowercase, uppercase and titlecase version of this concatinated version of names.

first_name = "robin"
last_name = "stardust"
full_name = first_name + " " + last_name

# Print lowercase version of full_name (O: robin stardust)
print(full_name.lower())
# Print uppercase version of full_name (O: ROBIN STARDUST)
print(full_name.upper())
# Print titlecase version of full_name (O: Robin Stardust)
print(full_name.title())
