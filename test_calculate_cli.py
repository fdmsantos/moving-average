import unittest
from src.events.Factory import Factory as EventFactory
from src.events.Event import Event
from datetime import datetime
from src.moving_average import MovingAverage


class CliTest(unittest.TestCase):
    """
        Unit tests
    """

    def test_ValidateEvent(self):
        """
            Test the Event function
        """
        event = dict()
        event["timestamp"] = "2018-12-26 18:11:08.509654"
        event["translation_id"] = "5aa5b2f39f7254a75aa5"
        event["source_language"] = "en"
        event["target_language"] = "fr"
        event["client_name"] = "easyjet"
        event["event_name"] = "translation_delivered"
        event["nr_words"] = 30
        event["duration"] = 20

        self.assertTrue(EventFactory.get_validations(event).handle_request(), "Test a good event")

        event_temp = dict(event)
        del event_temp["timestamp"]
        self.assertFalse(EventFactory.get_validations(event_temp).handle_request(), "Test timestamp missing")

        event_temp = dict(event)
        del event_temp["translation_id"]
        self.assertFalse(EventFactory.get_validations(event_temp).handle_request(), "Test translation_id missing event")

        event_temp = dict(event)
        del event_temp["source_language"]
        self.assertTrue(EventFactory.get_validations(event_temp).handle_request(), "Test source_language missing event")

        event_temp = dict(event)
        del event_temp["target_language"]
        self.assertFalse(EventFactory.get_validations(event_temp).handle_request(), "Test target_language missing event")

        event_temp = dict(event)
        del event_temp["client_name"]
        self.assertFalse(EventFactory.get_validations(event_temp).handle_request(), "Test client_name missing event")

        event_temp = dict(event)
        del event_temp["event_name"]
        self.assertFalse(EventFactory.get_validations(event_temp).handle_request(), "Test event_name missing event")

        event_temp = dict(event)
        del event_temp["nr_words"]
        self.assertFalse(EventFactory.get_validations(event_temp).handle_request(), "Test nr_words missing event")

        event_temp = dict(event)
        del event_temp["duration"]
        self.assertFalse(EventFactory.get_validations(event_temp).handle_request(), "Test duration missing event")

        event_temp = dict(event)
        event_temp["duration"] = "string"
        self.assertFalse(EventFactory.get_validations(event_temp).handle_request(), "Test duration string event")

        event_temp = dict(event)
        event_temp["nr_words"] = "string"
        self.assertFalse(EventFactory.get_validations(event_temp).handle_request(), "Test nr_words string event")

        event_temp = dict(event)
        event_temp["event_name"] = "translation_requested"
        self.assertFalse(EventFactory.get_validations(event_temp).handle_request(), "Test translation_delivered wrong value event")

        event_temp = dict(event)
        event_temp["timestamp"] = "2018-12-26"
        self.assertFalse(EventFactory.get_validations(event_temp).handle_request(), "Test timestamp bad format event")

    def test_movingAverage(self):
        window_size = 10
        events = list()
        events.append(Event(datetime.strptime("2018-12-26 18:11:08.509654", Event.TIMESTAMP_FORMAT),
                                    None, None, None, None, None,
                                    20,
                                    None))

        events.append(Event(datetime.strptime("2018-12-26 18:15:19.903159", Event.TIMESTAMP_FORMAT),
                                    None, None, None, None, None,
                                    31,
                                    None))

        events.append(Event(datetime.strptime("2018-12-26 18:23:19.903159", Event.TIMESTAMP_FORMAT),
                                    None, None, None, None, None,
                                    54,
                                    None))

        results = MovingAverage(events, window_size).calculate()

        self.assertEqual(len(results), 14, "Wrong size")

        self.assertEqual(results[0].date, "2018-12-26 18:11:00", "Wrong Date in Index 0")
        self.assertEqual(results[1].date, "2018-12-26 18:12:00", "Wrong Date in Index 1")
        self.assertEqual(results[2].date, "2018-12-26 18:13:00", "Wrong Date in Index 2")
        self.assertEqual(results[3].date, "2018-12-26 18:14:00", "Wrong Date in Index 3")
        self.assertEqual(results[4].date, "2018-12-26 18:15:00", "Wrong Date in Index 4")
        self.assertEqual(results[5].date, "2018-12-26 18:16:00", "Wrong Date in Index 5")
        self.assertEqual(results[6].date, "2018-12-26 18:17:00", "Wrong Date in Index 6")
        self.assertEqual(results[7].date, "2018-12-26 18:18:00", "Wrong Date in Index 7")
        self.assertEqual(results[8].date, "2018-12-26 18:19:00", "Wrong Date in Index 8")
        self.assertEqual(results[9].date, "2018-12-26 18:20:00", "Wrong Date in Index 9")
        self.assertEqual(results[10].date, "2018-12-26 18:21:00", "Wrong Date in Index 10")
        self.assertEqual(results[11].date, "2018-12-26 18:22:00", "Wrong Date in Index 11")
        self.assertEqual(results[12].date, "2018-12-26 18:23:00", "Wrong Date in Index 12")
        self.assertEqual(results[13].date, "2018-12-26 18:24:00", "Wrong Date in Index 13")

        self.assertEqual(results[0].average_delivery_time, 0 , "Wrong Date in Index 0")
        self.assertEqual(results[1].average_delivery_time, 20.0, "Wrong Average Delivery Time in Index 1")
        self.assertEqual(results[2].average_delivery_time, 20.0, "Wrong Average Delivery Time in Index 2")
        self.assertEqual(results[3].average_delivery_time, 20.0, "Wrong Average Delivery Time in Index 3")
        self.assertEqual(results[4].average_delivery_time, 20.0, "Wrong Average Delivery Time in Index 4")
        self.assertEqual(results[5].average_delivery_time, 25.5, "Wrong Average Delivery Time in Index 5")
        self.assertEqual(results[6].average_delivery_time, 25.5, "Wrong Average Delivery Time in Index 6")
        self.assertEqual(results[7].average_delivery_time, 25.5, "Wrong Average Delivery Time in Index 7")
        self.assertEqual(results[8].average_delivery_time, 25.5, "Wrong Average Delivery Time in Index 8")
        self.assertEqual(results[9].average_delivery_time, 25.5, "Wrong Average Delivery Time in Index 9")
        self.assertEqual(results[10].average_delivery_time, 25.5, "Wrong Average Delivery Time in Index 10")
        self.assertEqual(results[11].average_delivery_time, 31.0, "Wrong Average Delivery Time in Index 11")
        self.assertEqual(results[12].average_delivery_time, 31.0, "Wrong Average Delivery Time in Index 12")
        self.assertEqual(results[13].average_delivery_time, 42.5, "Wrong Average Delivery Time in Index 13")

        # for result in results:
        #     print(result)


if __name__ == '__main__':
    unittest.main()
