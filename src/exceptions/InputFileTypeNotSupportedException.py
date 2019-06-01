class InputFileTypeNotSupportedException(Exception):

    ''' Raise when the input type isn't supported '''
    def __init__(self, message):
        super(InputFileTypeNotSupportedException, self).__init__(message)
