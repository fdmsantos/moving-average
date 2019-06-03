from datetime import timedelta
from src.Result import Result
import logging
from src.aggregations.AggregationsAbstract import AggregationsAbstract


class MovingAverage(AggregationsAbstract):

    TYPE = "AVG"

    def calculate(self):
        logging.debug("calculating moving average")
        output = []
        date, end_date = self.get_start_end_date()
        logging.info("start date: " + date.strftime("%Y-%m-%d %H:%M:%S"))
        logging.info("finish date: " + end_date.strftime("%Y-%m-%d %H:%M:%S"))
        while date <= end_date:
            output.append(Result(date.strftime('%Y-%m-%d %H:%M:%S'), self.moving_average(date)))
            date += timedelta(minutes=1)
        return output

    def get_start_end_date(self):
        logging.debug("calculating start and end date")
        dates = [event.timestamp for event in self.events]
        return min(dates).replace(second=0, microsecond=0),  max(dates) + timedelta(minutes=1)

    def moving_average(self, date):
        durations = [event.duration for event in self.events if date - timedelta(minutes=self.window_size) < event.timestamp <= date]
        return sum(durations)/len(durations) if len(durations) > 0 else 0
