name1 = input("What is your name ? : ")
name2 = input("What is the other person's name ? : ")

name_mashup = f"{name1}{name2}".upper()

true_counts = {letter: name_mashup.count(letter) for letter in "TRUE"}
love_counts = {letter: name_mashup.count(letter) for letter in "LOVE"}

print(name_mashup)
print(true_counts)
print(love_counts)

true_love = int(f"{sum(true_counts.values())}{sum(love_counts.values())}")
print(true_love)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")
