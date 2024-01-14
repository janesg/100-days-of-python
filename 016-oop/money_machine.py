class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.balance = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.balance}")

    def process_coins(self) -> float:
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]

        return self.money_received

    def make_payment(self, cost):
        """Collect the necessary coins to pay the cost."""
        while self.money_received < cost:
            self.process_coins()
            print("Total inserted so far : ${:.2f}".format(self.money_received))

        change = round(self.money_received - cost, 2)
        print(f"Here is the {self.CURRENCY}{change} in change that you're owed.")
        self.balance += cost
        self.money_received = 0
