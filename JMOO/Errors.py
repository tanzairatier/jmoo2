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

"""Errors module for defining more-helpful friendly errors that may arise."""

class NullInputError(Exception):
    """Friendly exception for when a required non-null input was given as null.
    """
    def __init__(self, message="No input was provided, but was required."):
        super(NullInputError, self).__init__(message)

class DecisionOutOfBoundsError(Exception):
    """Friendly exception for when a decision variable attempts to set a value that is
    out of range with its defined min/max.
    """
    def __init__(self, message="Decision out of bounds."):
        super(DecisionOutOfBoundsError, self).__init__(message)

class ImproperInputError(Exception):
    """Friendly error when a required input was defined in the wrong way.  This could happen
    if the input was defined as the wrong type, the wrong list-size, etc.
    """
    def __init__(self, message="Input provided was incompatible with what was required."):
        super(ImproperInputError, self).__init__(message)

class DecisionVariableStructureError(Exception):
    """Friendly error for when decision variables were not properly defined; either they
    were not defined at all or they were defined in the wrong way.  Decision variables
    can only be defined as a list of *Decision* objects.
    """
    def __init__(self, message="Decision variables not set correctly."):
        super(DecisionVariableStructureError, self).__init__(message)

class ObjectiveStructureError(Exception):
    """Friendly error for when objectives were not properly defined; either because they
    were not defined at all or they were defined in the wrong way.  Objectives can only
    be defined as a list of *Objective* objects.
    """
    def __init__(self, message="Objectives not set correctly."):
        super(ObjectiveStructureError, self).__init__(message)

class ObjectiveNotEvaluatedError(Exception):
    """Friendly error for when an objective's fitness value was required, but it had not
    been yet evaluated.  Before an objective's fitness value (i.e. *value* member) is able
    to be retrieved, the objective must first be evaluated by the *Problem.evaluate* method.

    Furthermore, the objective's fitness value is only meant to be a temporary store of the
    objective's evaluation.  Fitnesses are more permanently stored in an *Individual* that
    subscribes to the problem evaluating the individual's decisions.
    """
    def __init__(self, message="Objective was not evaluated."):
        super(ObjectiveNotEvaluatedError, self).__init__(message)

class InvalidSetupError(Exception):
    """Friendly error for when you try to setup something in an incompatible way.  For
    example: setting up an algorithm to run with a stopping criteria that relies on a
    stat that was not set up for stat tracking."""
    def __init__(self, message="The setup was not valid and could not be used."):
        super(InvalidSetupError, self).__init__(message)

class DuplicateStatError(Exception):
    """Friendly error for when you try to set stats to track but you use the same
    stat more than once."""
    def __init__(self, message="Duplicate stats cannot be tracked."):
        super(DuplicateStatError, self).__init__(message)

class NonUniqueStatError(Exception):
    """Friendly error for when you set stats to track but some stat has the same
    name as another stat."""
    def __init__(self, message="Stats must have unique names."):
        super(NonUniqueStatError, self).__init__(message)