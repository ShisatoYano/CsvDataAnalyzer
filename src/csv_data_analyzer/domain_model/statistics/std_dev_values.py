# coding: utf-8

"""
StdDevValues class

Collect std dev value of each data

Author: Shisato Yano
"""

from .std_dev_value import StdDevValue


class StdDevValues:
    def __init__(self):
        self._collection = {}
        self._std_dev_value = StdDevValue()

    def add(self, data_name, array):
        self._collection[data_name] = self._std_dev_value.calculate(array)

    def get(self, data_name):
        return self._collection[data_name]
