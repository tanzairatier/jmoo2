from Friendly_Errors import ImproperInputError

class Variable(object):
    """base class for storing decisions or objectives"""
    def __init__(self, lower = None, upper = None, descript = ""):
        if not isinstance(lower, int) and not isinstance(lower, float):
            raise ImproperInputError()
        self.lower_bound = lower
        self.upper_bound = upper
        self.description = descript

