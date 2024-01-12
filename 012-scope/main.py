# These are global scope variables
counter_a = 1
counter_b = 7
counter_c = 5

def increase_count():
    # counter_a here is a new local scope variable
    counter_a = 2
    # counter_c here is the existing global scope variable
    global counter_c
    counter_c = 9
    print(f"Inside function, count A = {counter_a}")
    # Here, we're referencing the global scope variable without mutating it
    print(f"Inside function, count B = {counter_b}")
    print(f"Inside function, count C = {counter_c}")


increase_count()
print(f"Outside function, count A = {counter_a}")
print(f"Outside function, count B = {counter_b}")
print(f"Outside function, count C = {counter_c}")

# In python, there is no 'block scope' as there is in Java
# Scope is defined by:
#   - the enclosing function
# or if there is no enclosing function, the scope is global

# So, this code is valid because lack of enclosing function means my_var is global
if 3 > 2:
    my_var = 27

# ...but this would cause an error because my_var would never be defined
# if 3 < 2:
#     my_var = 27

print(f"my_var = {my_var}")


def outermost_func():
    outer_var = 11
    def outer_func():
        outer_var = 21
        def inner_func():
            # Using 'global' keyword here to try and refer to outer functions variable
            # does NOT work ... still thinks outer_var is a new local scope variable
            # global outer_var

            # Instead, we have to use the 'nonlocal' keyword
            # With multiple levels of nesting, this refers to the variable in the
            # immediate outer function
            nonlocal outer_var
            outer_var = 25
            inner_var = 30
            print(f"Inner func: outer var = {outer_var}")
            print(f"Inner func: inner var = {inner_var}")

        inner_func()
        print(f"Outer func: outer var = {outer_var}")
        # When running the program, the line below gives the error:
        #   "NameError: name 'inner_var' is not defined. Did you mean: 'outer_var'?"
        #   ...but the program still runs and just misses out this line in the output!
        # print(f"Outer func: inner var = {inner_var}")

    outer_func()
    print(f"Outermost func: outer var = {outer_var}")

outermost_func()

# Constants: standard is to use uppercase names
#   - nothing to stop code actually changing it though
PI = 3.14159