# coding: utf-8

"""
Test code  for StdDevValue class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.std_dev_value import StdDevValue


def test_std_dev_value():
    std_dev_value = StdDevValue()
    assert std_dev_value.calculate([5, 5, 5, 5, 5]) == 0
