# coding: utf-8

"""
Test code  for StdDevValues class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.std_dev_values import StdDevValues


def test_std_dev_values():
    collection = StdDevValues()
    collection.add("data", [5, 5, 5, 5, 5])
    assert collection.get("data") == 0
