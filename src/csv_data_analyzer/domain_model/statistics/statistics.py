# coding: utf-8

"""
Statistics class

Author: Shisato Yano
"""

from .maximum_values import MaximumValues
from .minimum_values import MinimumValues
from .mean_values import MeanValues
from .std_dev_values import StdDevValues


class Statistics:
    def __init__(self):
        self._maximum_values = MaximumValues()
        self._minimum_values = MinimumValues()
        self._mean_values = MeanValues()
        self._std_dev_values = StdDevValues()

    def calculate(self, data_frame, data_name_list):
        for data_name in data_name_list:
            self._maximum_values.add(data_name, data_frame[data_name].values)
            self._minimum_values.add(data_name, data_frame[data_name].values)
            self._mean_values.add(data_name, data_frame[data_name].values)
            self._std_dev_values.add(data_name, data_frame[data_name].values)

    def maximum_value(self, data_name):
        return self._maximum_values.get(data_name)

    def minimum_value(self, data_name):
        return self._minimum_values.get(data_name)

    def mean_value(self, data_name):
        return self._mean_values.get(data_name)

    def std_dev_value(self, data_name):
        return self._std_dev_values.get(data_name)
