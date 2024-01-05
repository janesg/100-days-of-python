import random

names_input = input("Enter a list of names separated by comma : ")
names = names_input.split(",")
names = [x.strip() for x in names]
print(names)

# select a name from the list at random
print(f"Looks like {names[random.randint(0, len(names) - 1)]} is paying for dinner !")