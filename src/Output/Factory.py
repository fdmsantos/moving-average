from src.Output import JsonWriter
from src.exceptions.OutputTypeNotSupportedException import OutputTypeNotSupportedException


class Factory(object):

    @staticmethod
    def write(output_type, results):
        Factory.get_writer_class(output_type).write(results)

    @staticmethod
    def get_writer_class(output_type):
        if output_type in JsonWriter.JsonWriter.TYPES:
            return JsonWriter.JsonWriter
        else:
            raise OutputTypeNotSupportedException("Output type not supported")
