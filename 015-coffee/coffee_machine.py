resources = {
    "water": {
        "amount": 300,
        "units": "ml"
    },
    "coffee": {
        "amount": 100,
        "units": "g"
    },
    "milk": {
        "amount": 200,
        "units": "ml"
    },
    "money": {
        "amount": 0,
        "units": "$"
    }
}

hot_drinks = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "price": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "price": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "price": 3
    }
}


def print_resources() -> None:
    print(f"Water: {resources['water']['amount']}{resources['water']['units']}")
    print(f"Milk: {resources['milk']['amount']}{resources['milk']['units']}")
    print(f"Coffee: {resources['coffee']['amount']}{resources['coffee']['units']}")
    print(f"Money: {resources['money']['units']}{resources['money']['amount']}")


def check_resources(drink: str) -> dict:
    deficient_in = {}

    if resources["water"]["amount"] < hot_drinks[drink]["ingredients"]["water"]:
        deficient_in["water"] = {
            "available": resources["water"]["amount"],
            "required": hot_drinks[drink]["ingredients"]["water"]
        }

    if resources["milk"]["amount"] < hot_drinks[drink]["ingredients"]["milk"]:
        deficient_in["milk"] = {
            "available": resources["milk"]["amount"],
            "required": hot_drinks[drink]["ingredients"]["milk"]
        }

    if resources["coffee"]["amount"] < hot_drinks[drink]["ingredients"]["coffee"]:
        deficient_in["coffee"] = {
            "available": resources["coffee"]["amount"],
            "required": hot_drinks[drink]["ingredients"]["coffee"]
        }

    return deficient_in


is_on = True
while is_on:
    drink = None
    request = input("What would you like ? [(e)spresso/(l)atte/(c)appuccino] : ").lower()[0]
    if request == 'e':
        drink = "espresso"
    elif request == 'l':
        drink = "latte"
    elif request == 'c':
        drink = "cappuccino"
    elif request == 'r':
        print_resources()
    elif request == 'x' or request == 'q':
        print("Switching off the coffee machine...")
        is_on = False
    else:
        print("You didn't specify a valid option... shame on you")

    if drink:
        low_resources = check_resources(drink)
        if len(low_resources) > 0:
            print(f"Sorry, unable to make your {drink} due to low resource(s):")
            for resource in low_resources:
                msg = (
                    f"{resource.capitalize()} : "
                    f"Needed: {low_resources[resource]["required"]}, "
                    f"Available: {low_resources[resource]["available"]}"
                )
                print(f"\t{msg}")

            continue
        total = 0
        while total < hot_drinks[drink]["price"]:
            print("Please insert coins to the full amount...")

            total += int(input(f"How many quarters ? : ")) * 0.25
            total += int(input(f"How many dimes ? : ")) * 0.1
            total += int(input(f"How many nickels ? : ")) * 0.05
            total += int(input(f"How many pennies ? : ")) * 0.01

            print("Total inserted so far : ${:.2f}".format(total))

        change = total - hot_drinks[drink]["price"]
        resources["money"]["amount"] += hot_drinks[drink]["price"]
        resources["water"]["amount"] -= hot_drinks[drink]["ingredients"]["water"]
        resources["milk"]["amount"] -= hot_drinks[drink]["ingredients"]["milk"]
        resources["coffee"]["amount"] -= hot_drinks[drink]["ingredients"]["coffee"]

        if change > 0.0:
            print("Here is the ${:.2f} in change that you're owed.".format(change))
        print(f"Here is your expertly brewed {drink} ... enjoy.")
