
def is_prime(number: int) -> bool:
    if number == 1:
        return True
    else:
        for i in range(number - 1, 1, -1):
            if number % i == 0:
                return False

        return True


num = int(input("Enter a number between 1 and 100 : "))

if num < 1 or num > 100:
    print(f"You entered an invalid value of {num}")
    exit(1)

print(f"The number, {num}, is {"" if is_prime(num) else "NOT "}a prime number")