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

"""This module contains the definition for the Variable base class."""

from FriendlyErrors import ImproperInputError 

class Variable(object):
    """Stores a variable that can have a boundary and description."""

    def __init__(self, lower=None, upper=None, descript=""):
        """Initializes a variable object with boundary and description.

        Args:
            lower: A float/int representing the lower boundary (inclusive)
            upper: A float/int representing the upper boundary (inclusive)
            descript: A string that describes the variable

        Returns:
            None

        Raises:
            ImproperInputError: If boundaries are not float/int, or if
            description is not a string, or if upper <= lower.
        """

        if not isinstance(lower, int) and not isinstance(lower, float):
            raise ImproperInputError("Lower boundary must be a float or int.")

        if not isinstance(upper, int) and not isinstance(upper, float):
            raise ImproperInputError("Upper boundary must be a float or int.")

        if not isinstance(descript, str):
            raise ImproperInputError("Description must be a string.")

        if upper <= lower:
            raise ImproperInputError("Upper boundary must be greater than lower \
                boundary.")

        self.lower_bound = lower
        self.upper_bound = upper
        self.description = descript
