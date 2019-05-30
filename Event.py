class Event(object):

    TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

    timestamp = None
    translation_id = None
    source_language = None
    target_language = None
    client_name = None
    event_name = None
    duration = None
    nr_words = None

    def __init__(self, timestamp, translation_id, source_language, target_language, client_name, event_name, duration, nr_words):
        self.timestamp = timestamp
        self.translation_id = translation_id
        self.source_language = source_language
        self.target_language = target_language
        self.client_name = client_name
        self.event_name = event_name
        self.duration = duration
        self.nr_words = nr_words

