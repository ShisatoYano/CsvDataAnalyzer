# coding: utf-8

"""
Test code  for MinimumValue class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.minimum_value import MinimumValue


def test_minimum_value():
    min_value = MinimumValue()
    assert min_value.calculate_minimum_value([1, 3, 5, 19, 8]) == 1
