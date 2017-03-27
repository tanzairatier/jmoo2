class Variable(object):
    """base class for storing decisions or objectives"""
    def __init__(self, lower = None, upper = None, descript = ""):
        self.lower_bound = lower
        self.upper_bound = upper
        self.description = descript

