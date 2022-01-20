# coding: utf-8

"""
Test code  for MaximumValue class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.maximum_value import MaximumValue


def test_maximum_value():
    max_value = MaximumValue()
    assert max_value.calculate([1, 3, 5, 19, 8]) == 19
