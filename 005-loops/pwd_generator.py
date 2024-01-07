import random

print("Welcome to the PyPassword Generator.")
num_letters = int(input("How many letters would you like in your password (12) ? ").strip() or "12")
num_symbols = int(input("How many symbols would you like (3) ? ").strip() or "3")
num_numbers = int(input("How many numbers would you like (2) ? ").strip() or "2")

letters = [chr(i) for i in range(97, 123)]
letters.extend([letter.upper() for letter in letters])
numbers = [chr(i) for i in range(48, 58)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Initialise all pwd characters to know value
pwd = ['£'] * num_letters

# Set the numbers and symbols first
random_ints = random.sample(range(0, len(pwd)), (num_numbers + num_symbols))

for i in range(0, len(random_ints)):
    if i < num_numbers:
        pwd[random_ints[i]] = numbers[random.randint(0, len(numbers) - 1)]
    else:
        pwd[random_ints[i]] = symbols[random.randint(0, len(symbols) - 1)]

for i in range(0, len(pwd)):
    if pwd[i] == '£':
        pwd[i] = letters[random.randint(0, len(letters) - 1)]

print(f"Your new password is: {"".join(pwd)}")
