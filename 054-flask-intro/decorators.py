# Functions inputs/functionality/outputs
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Functions are 1st class objects so can be passed around as arguments
def calculate(calc_func, n1, n2):
    return calc_func(n1, n2)


print(calculate(multiply, 3, 5))


# Nested functions... a function within a function
def outer() -> None:
    print("I'm outer")

    def inner():
        print("I'm inner")

    # inner function is only callable within scope of outer function
    inner()


outer()


# Function can return a function
def outer() -> ():
    print("I'm outer")

    def inner():
        print("I'm inner")

    # inner function is returned so that can be called from outside scope of outer function
    return inner


outer()()


# Decorator to delay running of function by 2 seconds in a separate thread
import time
import threading


def delay_decorator(func) -> ():
    def wrapper():
        # Use a separate thread to run the decorated function...main thread doesn't have to wait
        # Use 'or' to combine multiple statements in a lambda
        threading.Thread(target=(lambda: time.sleep(2) or func())).start()

    return wrapper


@delay_decorator
def say_hello():
    print("Hello")


def say_goodbye():
    print("Goodbye")


say_hello()
say_goodbye()
# Decorator @ is just syntactic sugar for:
delay_decorator(say_goodbye)()
time.sleep(5)