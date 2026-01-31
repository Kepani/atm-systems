class UserSession:
    MAX_PIN_TRIES = 3

    def __init__(self):
        self.card = None
        self.authenticated = False
        self.pin_tries = 0

    def reset(self):
        self.card = None
        self.authenticated = False
        self.pin_tries = 0
