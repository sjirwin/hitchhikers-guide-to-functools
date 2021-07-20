import statistics
from functools import cached_property
class DataSet:
    def __init__(self, sequence_of_numbers):
        self._data = tuple(sequence_of_numbers)
    @cached_property
    def stdev(self):
        return statistics.stdev(self._data)