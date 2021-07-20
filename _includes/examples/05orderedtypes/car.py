from functools import total_ordering
@total_ordering
class Car():
    def __init__(self, year, make, model):
        self.year, self.make, self.model = year, make, model
    def __eq__(self, o):
        if not isinstance(o, Car):
            return NotImplemented
        return ((self.year, self.make, self.model) == (o.year, o.make, o.model))
    def __lt__(self, o):
        if not isinstance(o, Car):
            return NotImplemented
        return ((self.year, self.make, self.model) < (o.year, o.make, o.model))