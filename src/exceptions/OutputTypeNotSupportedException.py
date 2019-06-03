class OutputTypeNotSupportedException(Exception):

    ''' Raise when the input type isn't supported '''
    def __init__(self, message):
        super(OutputTypeNotSupportedException, self).__init__(message)
