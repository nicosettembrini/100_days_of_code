MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# 1: Print Report
def report():
    """ Prints the ingredients remaining quantities """
    water_remaining = resources["water"]
    milk_remaining= resources["milk"]
    coffee_remaining = resources["coffee"]
    global profit 

    print(f"Water: {water_remaining}ml")
    print(f"Milk: {milk_remaining}ml")
    print(f"Coffee: {water_remaining}g")
    print(f"Profit: ${profit}")

def resources_remaining():
    """ Returns the ingredients remaining quantities """
    water_remaining = resources["water"]
    milk_remaining= resources["milk"]
    coffee_remaining = resources["coffee"]

    return water_remaining, milk_remaining, coffee_remaining

def check_coffee(coffee):
    water_remaining, milk_remaining, coffee_remaining = resources_remaining()
    if coffee != "espresso":
        if water_remaining < MENU[coffee]["ingredients"]["water"]:
            print("Sorry there's not enough water")
            return False
        elif coffee_remaining < MENU[coffee]["ingredients"]["coffee"]:
            print("Sorry there's not enough coffee")
            return False
        elif milk_remaining < MENU[coffee]["ingredients"]["milk"]:
            print("Sorry there's not enough milk")
            return False
        else:
            return True
    else:
        if water_remaining < MENU[coffee]["ingredients"]["water"]:
            print("Sorry there's not enough water")
            return False
        elif coffee_remaining < MENU[coffee]["ingredients"]["coffee"]:
            print("Sorry there's not enough coffee")
            return False
        else:
            return True

def check_money(coffee_ordered):
    input_quarters = int(input("How many quarters?: "))
    input_dimes = int(input("How many dimes?: "))
    input_nickles = int(input("How many nickles?: "))
    input_pennies = int(input("How many pennies?: "))   

    input_money = (input_quarters * 0.25) + (input_dimes * 0.10) + (input_nickles * 0.05) + (input_pennies * 0.01)

    cost = MENU[coffee_ordered]["cost"]
    change_money = input_money - cost

    if cost > input_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${change_money} in change.")
        print(f"Here is your {coffee_ordered}. Enjoy!")
        global profit 
        profit += cost
        return True

def make_coffee(coffee):
    if coffee != "espresso":
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    else:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]

profit = 0
exit_app = False

def coffee_machine():
    while exit_app == False:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order not in ["report", "off", "espresso", "latte", "cappuccino"]:
            print("That coffee is not available in this machine.")
        elif order == "report":
            report()
        elif order == "off":
            break
        else:
            if check_coffee(order):
                print("Please insert coins: ")
                if check_money(order):
                    make_coffee(order)

coffee_machine()

