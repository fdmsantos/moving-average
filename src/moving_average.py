from datetime import timedelta
from src.Result import Result


class MovingAverage(object):

    events = None
    window_size = None

    def __init__(self, events, window_size):
        self.events = events
        self.window_size = window_size

    def calculate(self):
        output = []
        date, end_date = self.get_start_end_date()
        while date <= end_date:
            output.append(Result(date.strftime('%Y-%m-%d %H:%M:%S'), self.moving_average(date)))
            date += timedelta(minutes=1)
        return output

    def get_start_end_date(self):
        dates = [event.timestamp for event in self.events]
        return min(dates).replace(second=0, microsecond=0),  max(dates) + timedelta(minutes=1)

    def moving_average(self, date):
        durations = [event.duration for event in self.events if date - timedelta(minutes=self.window_size) < event.timestamp <= date]
        return sum(durations)/len(durations) if len(durations) > 0 else 0
