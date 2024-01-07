year = int(input("Enter a year : "))

is_leap = False

if year % 400 == 0:
    is_leap = True
elif year % 4 == 0 and year % 100 != 0:
    is_leap = True

print(f"The year, {year}, is {"" if is_leap else "NOT "}a leap year")
