class CashDispenser:
    def __init__(self, initial_cash):
        self.cash = initial_cash

    def can_dispense(self, amount):
        return amount <= self.cash

    def dispense(self, amount):
        if not self.can_dispense(amount):
            raise ValueError("Insufficient cash in dispenser")

        self.cash -= amount
        return amount

    def get_balance(self):
        return self.cash