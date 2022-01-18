# coding: utf-8

"""
Test code for FileReader class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.file_reader.file_reader import FileReader


def test_init():
    reader = FileReader()
    assert reader.data_frame() is None


def test_data_frame():
    reader = FileReader()
    reader.read_csv_file("../data/sample.csv")
    df = reader.data_frame()
    assert df.columns.to_list()[0] == "rallyCnt"
