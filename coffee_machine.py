# Write your code here
class CoffeeMachine:
    water = 0
    milk = 0
    coffee = 0
    cups = 0
    cash = 0

    def __init__(self, water, milk, coffee, cups, cash):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.cash = cash

    def print_resources(self):
        print("""The coffee machine has:
        {} of water
        {} of milk
        {} of coffee beans
        {} of disposable cups
        ${} of money""".format(self.water, self.milk, self. coffee, self.cups, self.cash))

    def check_resources(self, coffee_type):
        if self.cups > 0:
            if coffee_type == "1":
                if self.water >= 250 and self.coffee >= 16:
                    return True
            elif coffee_type == "2":
                if self.water >= 350 and self.milk >= 75 and self.coffee >= 20:
                    return True
            elif coffee_type == "3":
                if self.water >= 200 and self.milk >= 100 and self.coffee >= 12:
                    return True
            else:
                return False
        else:
            return False


continuer = True
machine = CoffeeMachine(400, 540, 120, 9, 550)

while continuer:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "buy":
        achat = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino, back - return to the menu:")
        if not machine.check_resources(achat):
            print("Can't make this cup!")
        elif achat == "1":
            machine.water -= 250
            machine.coffee -= 16
            machine.cash += 4
            machine.cups -= 1
        elif achat == "2":
            machine.water -= 350
            machine.milk -= 75
            machine.coffee -= 20
            machine.cash += 7
            machine.cups -= 1
        elif achat == "3":
            machine.water -= 200
            machine.milk -= 100
            machine.coffee -= 12
            machine.cash += 6
            machine.cups -= 1
        elif achat == "back":
            #rien faire et retourner au debut
            print("Returning to menu")
        else:
            achat = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino:")
    elif action == "fill":
        add_water = input("Write how many ml of water do you want to add:")
        machine.water += int(add_water)
        add_milk = input("Write how many ml of milk do you want to add:")
        machine.milk += int(add_milk)
        add_coffee = input("Write how many grams of coffee beans do you want to add:")
        machine.coffee += int(add_coffee)
        add_cups = input("Write how many disposable cups of coffee do you want to add:")
        machine.cups += int(add_cups)
    elif action == "take":
        print("I gave you ${}".format(machine.cash))
        machine.cash = 0
    elif action == "remaining":
        machine.print_resources()
    elif action == "exit":
        continuer = False