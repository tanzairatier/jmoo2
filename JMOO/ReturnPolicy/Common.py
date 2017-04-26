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

"""Common return policies.  Use these to select which generation is returned as a result
of running an algorithm."""

import random
from ..Base import ReturnPolicy

class ReturnLastGeneration(ReturnPolicy):
    """Return the final generation's population."""
    def __init__(self):
        pass

    def elect_generation(self, stat_tracker):
        return stat_tracker.get_latest_stat("Population")

class ReturnEveryGeneration(ReturnPolicy):
    """Return the final generation's population."""
    def __init__(self):
        pass

    def elect_generation(self, stat_tracker):
        return stat_tracker.get_every("Population")

class ReturnEverything(ReturnPolicy):
    """Return the final generation's population."""
    def __init__(self):
        pass

    def elect_generation(self, stat_tracker):
        return stat_tracker.get_everything()