from src.input import InputAbstract
import json


class JsonReader(InputAbstract.InputAbstract):

    EXTENSIONS = [".json"]

    @staticmethod
    def read(file):
        return [json.loads(line) for line in file]
