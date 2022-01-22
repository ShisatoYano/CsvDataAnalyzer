# coding: utf-8

"""
MeanValues class

Collect mean value of each data

Author: Shisato Yano
"""

from .mean_value import MeanValue


class MeanValues:
    def __init__(self):
        self._collection = {}
        self._mean_value = MeanValue()

    def add(self, data_name, array):
        self._collection[data_name] = self._mean_value.calculate(array)

    def get(self, data_name):
        return self._collection[data_name]
