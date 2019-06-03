class AggregationNotSupportedException(Exception):

    ''' Raise when the input type isn't supported '''
    def __init__(self, message):
        super(AggregationNotSupportedException, self).__init__(message)
