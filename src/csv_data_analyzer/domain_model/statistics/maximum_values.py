# coding: utf-8

"""
MaximumValues class

Collect maximum value of each data

Author: Shisato Yano
"""

from .maximum_value import MaximumValue


class MaximumValues:
    def __init__(self):
        self._collection = {}
        self._max_value = MaximumValue()

    def add(self, data_name, array):
        self._collection[data_name] = self._max_value.calculate(array)

    def get(self, data_name):
        return self._collection[data_name]
