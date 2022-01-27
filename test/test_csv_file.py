# coding: utf-8

"""
Test code for CsvFile class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.read.csv_file import CsvFile


def test_path():
    csv_obj = CsvFile("test.csv")
    assert csv_obj.path() == "test.csv"


def test_readable():
    csv_obj = CsvFile("test.csv")
    assert csv_obj.is_readable() is True


def test_not_readable():
    csv_obj = CsvFile("test.txt")
    assert csv_obj.is_readable() is False
