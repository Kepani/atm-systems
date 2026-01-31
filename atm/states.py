from enum import Enum, auto

class ATMState(Enum):
    IDLE = auto()
    CARD_INSERTED = auto()
    AUTHENTICATED = auto()
    TRANSACTION = auto()
    EJECT_CARD = auto()
