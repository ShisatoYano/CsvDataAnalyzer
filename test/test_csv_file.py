# coding: utf-8

"""
Test code for CsvFile class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.csv_file.csv_file import CsvFile


def test_readable_file_path():
    csv_obj = CsvFile("test.csv")
    assert csv_obj.file_path() == "test.csv"


def test_not_readable_file_path():
    not_csv_obj = CsvFile("test.txt")
    assert not_csv_obj.file_path() == ""
