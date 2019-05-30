from Output import OutputAbstract
import json


class JsonWriter(OutputAbstract.OutputAbstract):

    @staticmethod
    def write(results):
        for result in results:
            print(json.dumps(result.__dict__))
