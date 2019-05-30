from Input import InputAbstract
import json


class JsonReader(InputAbstract.InputAbstract):

    EXTENSIONS = [".json"]

    @staticmethod
    def read(filename):
        try:
            with open(filename) as json_file:
                data = [json.loads(line) for line in json_file]
            return data
        except:
            print("ERROR: specified input file not found or no permission to read")
