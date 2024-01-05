import random
# import my_module
from my_module import pi

random_int = random.randint(1, 10)
print(random_int)

# print(my_module.pi)
print(pi)

random_flt = random.random()
# Range is 0.00000... -> 0.999999...
print(random_flt)

# Range is 0.00000... -> 4.999999...
print(random_flt * 5)