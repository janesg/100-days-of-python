class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
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
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']['amount']}{self.resources['water']['units']}")
        print(f"Milk: {self.resources['milk']['amount']}{self.resources['milk']['units']}")
        print(f"Coffee: {self.resources['coffee']['amount']}{self.resources['coffee']['units']}")

    def check_resources(self, drink):
        """Returns a dictionary describing each insufficient resource for making given drink."""
        deficient_in = {}

        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]["amount"]:
                deficient_in[item] = {
                    "available": self.resources[item]["amount"],
                    "required": drink.ingredients[item]
                }

        return deficient_in

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item]["amount"] -= order.ingredients[item]

        print(f"Here is your expertly brewed {order.name} ☕️. Enjoy!")
