import time


def timing_decorator(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(f"Decorated function {func.__name__} took {t2 - t1} secs to run")

    return wrapper


@timing_decorator
def fast():
    for i in range(1000000):
        i * i


@timing_decorator
def slow():
    for i in range(10000000):
        i * i


fast()
slow()