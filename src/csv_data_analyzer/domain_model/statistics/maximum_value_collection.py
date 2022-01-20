# coding: utf-8

"""
MaximumValueCollection class

Collect maximum value of each data
"""

from .maximum_value import MaximumValue


class MaximumValueCollection:
    def __init__(self):
        self.collection = {}
        self.maxv = MaximumValue()

    def add(self, data_name, array):
        self.collection[data_name] = self.maxv.calculate(array)

    def get(self, data_name):
        return self.collection[data_name]
