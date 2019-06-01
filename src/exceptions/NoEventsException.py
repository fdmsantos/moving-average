class NoEventsException(Exception):

    ''' Raise when a file with no valid events is submitted '''
    def __init__(self, message):
        super(NoEventsException, self).__init__(message)
