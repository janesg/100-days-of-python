inputs = eval(input("Enter 3 comma-separated integers: "))
print(inputs)


def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(args[0], args[1], args[2])
        print(f"It returned {result}")
        return result

    return wrapper


@logging_decorator
def multiplier(a, b, c):
    return a * b * c


print(f"Result = {multiplier(inputs[0], inputs[1], inputs[2])}")
