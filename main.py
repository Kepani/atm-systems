from atm.atm import ATM
from atm.services.mock_bank import MockBankService

def main():
    bank = MockBankService()
    atm = ATM(bank)

    atm.insert_card("123")

    if atm.enter_pin("1111"):
        print("✅ Authenticated")
    else:
        print("❌ Invalid PIN")

if __name__ == "__main__":
    main()
