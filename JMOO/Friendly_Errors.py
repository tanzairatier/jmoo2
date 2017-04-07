

class NullInputError(Exception):
    def __init__(self, message="No input was provided, but was required."):
        super(NullInputError, self).__init__(message)


class DecisionOutOfBoundsError(Exception):
    def __init__(self, message="Input out of bounds."):
        super(DecisionOutOfBoundsError, self).__init__(message)

class ImproperInputError(Exception):
    def __init__(self, message="Input provided was incompatible with what was required."):
        super(ImproperInputError, self).__init__(message)