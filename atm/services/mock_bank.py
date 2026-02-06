class MockBankService:
    def __init__(self):
        self.accounts = {
            "123": {
                "pin": "1111",
                "balance": 1000
            }
        }

    def validate_pin(self, card_id, pin):
        return (
            card_id in self.accounts
            and self.accounts[card_id]["pin"] == pin
        )

<<<<<<< HEAD
    print("MockBankService Loaded")
=======
print("MockBankService Loaded")
>>>>>>> 95b83a723efc20671b9af2c0e1b5c41bf5304d6c
