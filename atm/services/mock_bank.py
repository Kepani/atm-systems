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

print("MockBankService Loaded")