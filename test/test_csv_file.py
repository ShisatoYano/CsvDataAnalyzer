# coding: utf-8

"""
Test code for CsvFile class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.csv_file.csv_file import CsvFile


def test_is_readable():
    csv_obj = CsvFile()
    assert csv_obj.is_readable("test.csv") is True


def test_is_not_readable():
    csv_obj = CsvFile()
    assert csv_obj.is_readable("test.txt") is False
