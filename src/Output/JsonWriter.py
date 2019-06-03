from src.Output import OutputAbstract
import json
import logging


class JsonWriter(OutputAbstract.OutputAbstract):

    TYPES = ["json"]

    @staticmethod
    def write(results):
        for result in results:
            logging.info(json.dumps(result.__dict__))
            print(json.dumps(result.__dict__))
