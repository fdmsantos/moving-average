import os
from Input import JsonReader
from Event import Event
from datetime import datetime
from IsRequired import IsRequired
from IsInteger import IsInteger
from IsEquals import IsEquals
from IsDateTimeFormat import IsDateTimeFormat


class Factory(object):

    @staticmethod
    def create_from_file(filename):
        # TODO Exception No Events
        return Factory.create_events(
            Factory.get_reader_class(filename).read(
                open(filename, "r")
            )
        )

    @staticmethod
    def create_events(events):
        events_objects = []
        for event in events:

            if Factory.get_validations(event).handle_request():
                events_objects.append(Event(datetime.strptime(event["timestamp"], Event.TIMESTAMP_FORMAT),
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

    @staticmethod
    def get_validations(event):
        rule1 = IsRequired(event, "timestamp")
        rule2 = IsRequired(event, "translation_id", rule1)
        rule3 = IsRequired(event, "source_language", rule2)
        rule4 = IsRequired(event, "target_language", rule3)
        rule5 = IsRequired(event, "client_name", rule4)
        rule6 = IsRequired(event, "event_name", rule5)
        rule7 = IsRequired(event, "duration", rule6)
        rule8 = IsRequired(event, "nr_words", rule7)
        rule9 = IsInteger(event, "duration", rule8)
        rule10 = IsInteger(event, "nr_words", rule9)
        rule11 = IsEquals(event, "event_name", rule10, "translation_delivered")
        rule12 = IsDateTimeFormat(event, "timestamp", rule11, Event.TIMESTAMP_FORMAT)
        return rule12
