from abc import ABC, abstractmethod


class AggregationsAbstract(ABC):

    events = None
    window_size = None

    def __init__(self, events, window_size):
        self.events = events
        self.window_size = window_size

    @abstractmethod
    def calculate(self):
        """Required Method"""
