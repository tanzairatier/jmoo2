from Variable import Variable

class Decision(Variable):
    """class for storing decisions for problems"""
    def __init__(self, lower = None, upper = None, descript = "", less_is_more = True):
        Variable.__init__(self, lower, upper, descript)