# coding: utf-8

"""
Test code  for StdDevValueCollection class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.std_dev_value_collection import StdDevValueCollection


def test_std_dev_value_collection():
    collection = StdDevValueCollection()
    collection.add("data", [5, 5, 5, 5, 5])
    assert collection.get("data") == 0
