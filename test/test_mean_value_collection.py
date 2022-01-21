# coding: utf-8

"""
Test code  for MeanValueCollection class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.mean_value_collection import MeanValueCollection


def test_mean_value_collection():
    collection = MeanValueCollection()
    collection.add("data", [5, 5, 5, 5, 5])
    assert collection.get("data") == 5
