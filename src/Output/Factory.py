from src.Output import JsonWriter


class Factory(object):

    @staticmethod
    def print(output_type, results):
        Factory.get_writer_class(output_type).write(results)

    @staticmethod
    def get_writer_class(output_type):
        # TODO Invalid Extension
        if output_type in JsonWriter.JsonWriter.TYPES:
            return JsonWriter.JsonWriter
