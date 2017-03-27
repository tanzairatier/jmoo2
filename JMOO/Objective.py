from Variable import Variable

class Objective(Variable):
    """class for storing objectives for problems"""
    def __init__(self, lower = None, upper = None, descript = "", less_is_more = True):
        Variable.__init__(self, lower, upper, descript)
        self.less_is_more = less_is_more
