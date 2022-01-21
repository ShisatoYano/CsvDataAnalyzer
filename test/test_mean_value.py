# coding: utf-8

"""
Test code  for MeanValue class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.mean_value import MeanValue


def test_mean_value():
    mean_value = MeanValue()
    assert mean_value.calculate([5, 5, 5, 5, 5]) == 5
