# coding: utf-8

"""
Test code for FileReader class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.file_reader.file_reader import FileReader


def test_data_frame():
    reader = FileReader("../data/sample.csv")
    assert reader.data_name_list()[0] == "rallyCnt"


def test_data_array():
    reader = FileReader("../data/sample.csv")
    assert reader.data_array("rallyCnt")[0] == 2
    assert reader.data_array("rallyCnt")[-1] == 2
