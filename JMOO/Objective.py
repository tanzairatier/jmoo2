# This file is part of JMOO.
#
#    JMOO is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    JMOO is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with JMOO.  If not, see < http: // www.gnu.org / licenses / >.

"""This module contains the base class for defining an objective, as well as its
commonly shared methods across all objective-related operations."""

import math
from Variable import Variable

class Objective(Variable):
    """Class for storing objectives for problems."""

    def __init__(self, descript="", less_is_more=True):
        Variable.__init__(self, -math.inf, math.inf, descript)
        self.less_is_more = less_is_more
