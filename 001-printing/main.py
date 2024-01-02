# Coding exercise 1 - basic print
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Multi-line
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

# Concatenation
print("Day 1 - Python Print Function" + "\nThe function is declared like this:" + "\nprint('what to print')")

# Using input function
name = input("What is your name ?\n")
print("Your name is " + name)
print("...and has " + str(len(name)) + " characters")

# Coding exercise 2 - variable value switch
input1 = input("Enter 1st value: ")
input2 = input("Enter 2nd value: ")

print(f"You entered: Value 1 = {input1}, Value 2 = {input2}")
input_temp = input1
input1 = input2
input2 = input_temp
print(f"Now swapped: Value 1 = {input1}, Value 2 = {input2}")

