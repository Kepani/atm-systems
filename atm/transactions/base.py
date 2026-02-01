from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, account_id):
        self.account_id = account_id

    @abstractmethod
    def execute(self):
        pass
