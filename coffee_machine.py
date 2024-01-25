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
    "money" : 0
}


def report():
    for key, value in resources.items():
        print(f"{key}: {value}")

def check_resources(drink):
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water")
        return False
    if drink != "espresso":
        if MENU[drink]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk")
            return False
    if MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    else: 
        return True
    

def process_coins(drink):
    print("Please insert coins. \n")
    quarters = int(input("How many quarters? : " ))
    dimes =    int(input("How many dimes?    : " ))
    nickles =  int(input("How many nickles?  : " ))
    pennies =  int(input("How many pennies?  : " ))
    total_coin_value = round((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies), 2)
    drink_cost = round(MENU[drink]["cost"], 2)
    if total_coin_value < drink_cost:
        print("\n Sorry that's not enough money. Money refunded. \n")
        return False
    elif total_coin_value > drink_cost:
        resources["money"] = resources["money"] + drink_cost
        change = round(total_coin_value - drink_cost, 2)
        print(f"\n Here is ${change} in change \n")
        return True
    elif total_coin_value == drink_cost:
        resources["money"] = resources["money"] + drink_cost
        return True
    else:
        print("something with coin processing went wrong")

def deduct_ingred(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"] 
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"] 


machine_on = True
while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "espresso" or order == "latte" or order == "cappuccino":
        if check_resources(order):
            if process_coins(order):
                deduct_ingred(order)
                print(f"Here is your {order} ☕️. Enjoy! \n")
    elif order == "report":
        report()
    elif order == "off":
        machine_on = False
    else:
        print("please choose from espresso/latte/cappuccino/report.")

