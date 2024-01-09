import math


def paint_calc(height: float, width: float, coverage: float) -> float:
    return (height * width) / coverage


h = float(input("Height (in m): "))
w = float(input("Width (in m): "))
coverage_per_can = float(input("Coverage per can (in metres squared): "))

result: float = paint_calc(h, w, coverage_per_can)
print(f"You'll need {math.ceil(result)} cans of paint")