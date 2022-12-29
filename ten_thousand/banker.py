
class Banker:
    # banker is responsible for tracking points on the shelf and in the bank

    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def bank(self):
        # adding shelved amount to balance
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def shelf(self, amount):
        # adding points to the shelf
        self.shelved += amount

    def clear_shelf(self):
        # reset the shelf to 0
        self.shelved = 0