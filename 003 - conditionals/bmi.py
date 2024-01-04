height = input("Enter your height in metres (e.g. 1.65): ")
weight = input("Enter your weight in kilograms (e.g. 74.2): ")

bmi = float(weight) / (float(height) ** 2)

health = "Ideal Weight"

if bmi > 35:
    health = "Clinically Obese"
elif bmi > 30:
    health = "Obese"
elif bmi > 25:
    health = "Slightly Overweight"
elif bmi < 18.5:
    health = "Under Weight"

print(f"Your BMI is {round(bmi, 2)} and you are considered {health}")