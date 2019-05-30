from abc import ABC, abstractmethod


class InputAbstract(ABC):

    @staticmethod
    @abstractmethod
    def read(filename):
        """Required Method"""
