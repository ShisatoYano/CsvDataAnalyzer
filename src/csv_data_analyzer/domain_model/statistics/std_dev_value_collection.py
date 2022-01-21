# coding: utf-8

"""
StdDevValueCollection class

Collect std dev value of each data

Author: Shisato Yano
"""

from .std_dev_value import StdDevValue


class StdDevValueCollection:
    def __init__(self):
        self.collection = {}
        self.std_dev_value = StdDevValue()

    def add(self, data_name, array):
        self.collection[data_name] = self.std_dev_value.calculate(array)

    def get(self, data_name):
        return self.collection[data_name]
