# coding: utf-8

"""
Test code  for MinimumValueCollection class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.minimum_value_collection import MinimumValueCollection


def test_minimum_value_collection():
    collection = MinimumValueCollection()
    collection.add("data", [1, 3, 5, 19, 8])
    assert collection.get("data") == 1
