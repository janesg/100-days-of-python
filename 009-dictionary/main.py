test_dict = {
    "Bug": "An error in a program",
    "Function": "A unit of code that can be called"
}

print(f"Dictionary keys: {test_dict.keys()}")
print(f"Dictionary values: {test_dict.values()}")

found = False

while not found:
    try:
        error_value = test_dict["Error"]
        found = True
        print(f"An error is {error_value.lower()}")
    except KeyError:
        print("There is no key of 'Error' in the dictionary. Adding one...")
        test_dict["Error"] = "A condition where something went wrong"

print(f"A bug is {test_dict["Bug"].lower()}")

# Iterating through a dictionary gives the keys (not each element)
for key in test_dict:
    print(f"Key: {key} - Value: {test_dict[key]}")

# Nested structures
travel_log_dict = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

travel_log_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]



