class Banker:

    def __init__(self, balance=0, shelved=0):
        self.balance = balance
        self.shelved = shelved

    def shelf(self, points):
        """
        INPUT >> Integer - amount of points to add to shelf
        OUTPUT >> No Output - adding points to shelved
        """
        self.shelved += points

    def bank(self):
        """
        INPUT >> no input
        OUTPUT >> Integer - the amount from the shelf
            - adding the shelved amount to balance
            - reset shelved to zero
        """
        temp_shelved = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return temp_shelved

    def clear_shelf(self):
        """
        INPUT >> NONE
        OUTPUT >> NONE
            - reset the shelved to zero
        """
        self.shelved = 0