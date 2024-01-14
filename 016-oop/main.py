from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

switched_on = True

while switched_on:
    drink: MenuItem = None
    item_names = menu.get_item_names()
    request = input(f"What would you like ? [{"/".join(item_names)}] : ").lower()[0]
    for name in item_names:
        if request == name[0]:
            drink = menu.find_drink(name)

    if drink:
        low_resources = cm.check_resources(drink)
        if len(low_resources) > 0:
            print(f"Sorry, unable to make your {drink.name} due to low resource(s):")
            for resource in low_resources:
                msg = (
                    f"{resource.capitalize()} - "
                    f"Needed: {low_resources[resource]["required"]}, "
                    f"Available: {low_resources[resource]["available"]}"
                )
                print(f"\t{msg}")

            continue

        mm.make_payment(drink.cost)
        cm.make_coffee(drink)
    elif request == 'r':
        cm.report()
        mm.report()
    elif request == 'x' or request == 'q':
        print("Switching off the coffee machine...")
        switched_on = False
    else:
        print("You didn't specify a valid option... shame on you")
