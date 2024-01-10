def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    x = float(input("Enter the first number : "))

    for operation in operations:
        print(operation)

    while True:
        op = input("Choose an operation : ")
        y = float(input("Enter the next number : "))
        result = operations[op](x, y)
        print(f"{x} {op} {y} = {result}")
        action = input(f"Type 'y' to continue calc with {result}, 'n' for new calc or 'x' to exit : ")
        if action == 'x':
            exit(0)
        elif action == 'y':
            x = result
        else:
            calculator()

calculator()