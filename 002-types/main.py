# Add together the digits of a 2 digit number
two_digit_number = input("Enter a 2 digit number : ")
number_str = str(two_digit_number)
sum = int(number_str[0]) + int(number_str[1])
print("The digits of your number add up to " + str(sum))
