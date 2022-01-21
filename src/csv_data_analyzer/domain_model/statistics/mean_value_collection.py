# coding: utf-8

"""
MeanValueCollection class

Collect mean value of each data
"""

from .mean_value import MeanValue


class MeanValueCollection:
    def __init__(self):
        self.collection = {}
        self.mean_value = MeanValue()

    def add(self, data_name, array):
        self.collection[data_name] = self.mean_value.calculate(array)

    def get(self, data_name):
        return self.collection[data_name]
