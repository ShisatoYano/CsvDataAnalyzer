# coding: utf-8

"""
Test code  for MinimumValues class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.minimum_values import MinimumValues


def test_minimum_values():
    collection = MinimumValues()
    collection.add("data", [1, 3, 5, 19, 8])
    assert collection.get("data") == 1
