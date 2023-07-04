MENU = {"espresso": {"ingredients": {"water": 50, "coffee": 18,},"cost": 1.5},
        "latte": {"ingredients": { "water": 200,"milk": 150,"coffee": 24,},"cost": 2.5},
        "cappuccino": {"ingredients": {"water": 250,"milk": 100,"coffee": 24,},"cost": 3.0}
       }
profit = 0
resources = {"water": 300,"milk": 200,"coffee": 100}
is_on = True
def is_resource_sufficient(order_indegredint):
    for item in order_indegredint:
        if order_indegredint[item]>=resources[item]:
            print(f"sorry there is not enough resources {item}.")
            return False
    return True
def is_tranjection(money_recived, drink_cost):
    if money_recived>=drink_cost:
        change = round(money_recived - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        
        print(" sorry that's not enough money. Money refunded.")
        return False
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def process_coin():
    print("please enter coin.")
    total = int(input("how many quaters"))*0.25
    total += int(input("how many dines"))*0.1
    total += int(input("how many nickles"))*0.05
    total += int(input("how many pennies"))*0.01
    return total

while is_on:
    choice = input("what would you want (espresso/latte/cappuccino) ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}g")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_tranjection(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])