from atm.states import ATMState
from atm.session import UserSession

class ATM:
    def __init__(self, bank_service):
        self.state = ATMState.IDLE
        self.session = UserSession()
        self.bank_service = bank_service

    def insert_card(self, card_id):
        if self.state != ATMState.IDLE:
            raise Exception("ATM not ready")

        self.session.card = card_id
        self.state = ATMState.CARD_INSERTED

    def enter_pin(self, pin):
        if self.state != ATMState.CARD_INSERTED:
            raise Exception("No card inserted")

        if self.bank_service.validate_pin(self.session.card, pin):
            self.session.authenticated = True
            self.state = ATMState.AUTHENTICATED
            return True

        self.session.pin_tries += 1

        if self.session.pin_tries >= UserSession.MAX_PIN_TRIES:
            self.eject_card()

        return False

    def eject_card(self):
        self.session.reset()
        self.state = ATMState.IDLE
