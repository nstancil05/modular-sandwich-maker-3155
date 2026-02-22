import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    is_active = True
    while is_active:
        choice = input("What would you like? (small/ medium/ large/ off): ").lower()
        if choice == "off":
            is_active = False
        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                print("The cost of a", choice, "sandwich is $" + str(sandwich["cost"]))
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Sorry that is not a valid option.")

# prevents accidental running of main
if __name__=="__main__":
    main()