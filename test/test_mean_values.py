# coding: utf-8

"""
Test code  for MeanValueCollection class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.mean_values import MeanValues


def test_mean_value_collection():
    collection = MeanValues()
    collection.add("data", [5, 5, 5, 5, 5])
    assert collection.get("data") == 5
