height = input("Enter your height in metres (e.g. 1.65): ")
weight = input("Enter your weight in kilograms (e.g. 74.2): ")

bmi = float(weight) / (float(height) ** 2)

# print("Your BMI = " + str(round(bmi, 2)))
print(f"Your BMI = {round(bmi, 2)}")