from src.aggregations.MovingAverage import MovingAverage
from src.exceptions.AggregationNotSupportedException import AggregationNotSupportedException


class Factory(object):

    @staticmethod
    def calculate(type, events, window_size):

        if type == MovingAverage.TYPE:
            aggregation = MovingAverage(
                events,
                window_size
            )
        else:
            raise AggregationNotSupportedException("Aggregation Type not supported")
        return aggregation.calculate()
