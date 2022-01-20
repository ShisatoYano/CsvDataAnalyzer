# coding: utf-8

"""
Test code  for MaximumValueCollection class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.maximum_value_collection import MaximumValueCollection


def test_maximum_value_collection():
    collection = MaximumValueCollection()
    collection.add("data", [1, 3, 5, 19, 8])
    assert collection.get("data") == 19
