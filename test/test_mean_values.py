# coding: utf-8

"""
Test code  for MeanValues class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.mean_values import MeanValues


def test_mean_values():
    collection = MeanValues()
    collection.add("data", [5, 5, 5, 5, 5])
    assert collection.get("data") == 5
