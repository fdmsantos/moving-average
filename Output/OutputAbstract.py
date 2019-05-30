from abc import ABC, abstractmethod


class OutputAbstract(ABC):

    @staticmethod
    @abstractmethod
    def write(results):
        """Required Method"""
