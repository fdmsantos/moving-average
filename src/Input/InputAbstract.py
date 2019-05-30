from abc import ABC, abstractmethod


class InputAbstract(ABC):

    @staticmethod
    @abstractmethod
    def read(file):
        """Required Method"""
