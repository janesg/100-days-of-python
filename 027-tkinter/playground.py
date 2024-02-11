def add(*args: int) -> int:
    # args is a tuple
    return sum(args)


print(add(1,2,3,4,5,6))


def calculate(n: int, **kwargs: int) -> int:
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(f"{key}:{value}")
    # print(kwargs['multiply'])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(15, add=3, multiply=5))