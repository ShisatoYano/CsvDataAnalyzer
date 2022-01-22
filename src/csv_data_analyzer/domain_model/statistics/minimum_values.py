# coding: utf-8

"""
MinimumValues class

Collect minimum value of each data

Author: Shisato Yano
"""

from .minimum_value import MinimumValue


class MinimumValues:
    def __init__(self):
        self._collection = {}
        self._min_value = MinimumValue()

    def add(self, data_name, array):
        self._collection[data_name] = self._min_value.calculate(array)

    def get(self, data_name):
        return self._collection[data_name]
