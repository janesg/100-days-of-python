days_in_month_by_leap_year = {
    True: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    False: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
}
year = int(input("Enter a year : "))
month = int(input("Enter a month ... 1 for Jan, 2 for Feb etc. : "))

is_leap = False

if year % 400 == 0:
    is_leap = True
elif year % 4 == 0 and year % 100 != 0:
    is_leap = True

print(f"There are {days_in_month_by_leap_year[is_leap][month - 1]} days in month {month} of {year}")