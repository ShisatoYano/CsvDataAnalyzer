# coding: utf-8

"""
MinimumValueCollection class

Collect minimum value of each data

Author: Shisato Yano
"""

from .minimum_value import MinimumValue


class MinimumValueCollection:
    def __init__(self):
        self.collection = {}
        self.min_value = MinimumValue()

    def add(self, data_name, array):
        self.collection[data_name] = self.min_value.calculate(array)

    def get(self, data_name):
        return self.collection[data_name]
