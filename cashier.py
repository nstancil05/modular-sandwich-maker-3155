class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from payment inserted."""
        print("Please insert payment.")
        total = int(input("how many single dollars?: ")) * 1.00
        total += int(input("how many half dollars?: ")) * 0.50
        total += int(input("how many quarters?: ")) * 0.25
        total += int(input("how many nickels?: ")) * 0.05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money.")
            return False