from abc import ABC, abstractmethod


class RuleAbstract(ABC):

    event = None
    field = None
    value = None

    def __init__(self, event, field, successor=None, value=None):
        self.event = event
        self._successor = successor
        self.field = field
        self.value = value

    @abstractmethod
    def handle_request(self):
        pass
