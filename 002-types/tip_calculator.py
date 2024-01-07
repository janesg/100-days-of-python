print("Welcome to the tip calculator.")
total = float(input("What was the total bill ? "))
split = int(input("How many people are splitting the bill ? "))
percentage_tip = float(input("What percentage tip would you like to give ? 10, 12 or 15 ? "))

per_person = (total * (1 + (percentage_tip / 100))) / split

# Note: this won't always give us 2 decimal places (i.e. if zero)
# print("Each person should pay: " + str(round(per_person, 2)))

print("Each person should pay: {:.2f}".format(round(per_person, 2)))