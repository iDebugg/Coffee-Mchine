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

total_money = 0


should_continue = True

def coffee_machine():
    return
while should_continue :
    ask_for_report = input("What would you like? (espresso/latte/cappuccino): ")
    if ask_for_report == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")
        print(f"Money : ${total_money}")
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_type == "espresso" :
            print("we are getting there")
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - 0
            total_money = total_money + MENU["espresso"]["cost"]

        elif coffee_type == "latte" :
            print("we are getting there")
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            total_money = total_money + MENU["latte"]["cost"]


        elif coffee_type == "cappuccino" :
            print("we are getting there")
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            total_money = total_money + MENU["cappuccino"]["cost"]





        else:
            should_continue = False


    else :
        coffee_machine()

coffee_machine()