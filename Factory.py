import os
from Input import JsonReader
from Event import Event
from datetime import datetime


class Factory(object):

    @staticmethod
    def create_from_file(filename):
        return Factory.create_events(
            Factory.get_reader_class(filename).read(
                open(filename, "r")
            )
        )

    @staticmethod
    def create_events(events):
        # TODO Validations
        events_objects = []
        for event in events:
            events_objects.append(Event(datetime.strptime(event["timestamp"], '%Y-%m-%d %H:%M:%S.%f'),
                                event["translation_id"],
                                event["source_language"],
                                event["target_language"],
                                event["client_name"],
                                event["event_name"],
                                event["duration"],
                                event["nr_words"]))
        return events_objects

    @staticmethod
    def get_reader_class(filename):
        _, file_extension = os.path.splitext(filename)
        # TODO Invalid Extension
        if file_extension in JsonReader.JsonReader.EXTENSIONS:
            return JsonReader.JsonReader
