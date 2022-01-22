# coding: utf-8

"""
Test code for Statistics class

Author: Shisato Yano
"""


import pandas as pd
import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.statistics.statistics import Statistics


def test_calculate_maximum():
    data_dict = dict(data1=[1, 2, 3, 4, 5],
                     data2=[10, 6, 3, 8, 1],
                     data3=[32, 3, 100, 59, 2])
    data_df = pd.DataFrame(data_dict)

    stats = Statistics()
    stats.calculate(data_df, tuple(data_df.columns.to_list()))
    assert stats.maximum_value("data1") == 5
    assert stats.maximum_value("data2") == 10
    assert stats.maximum_value("data3") == 100


def test_calculate_minimum():
    data_dict = dict(data1=[1, 2, 3, 4, 5],
                     data2=[10, 6, 3, 8, 4],
                     data3=[32, 67, 100, 59, 44])
    data_df = pd.DataFrame(data_dict)

    stats = Statistics()
    stats.calculate(data_df, tuple(data_df.columns.to_list()))
    assert stats.minimum_value("data1") == 1
    assert stats.minimum_value("data2") == 3
    assert stats.minimum_value("data3") == 32


def test_calculate_mean():
    data_dict = dict(data1=[1, 1, 1, 1, 1],
                     data2=[22, 22, 22, 22, 22],
                     data3=[333, 333, 333, 333, 333])
    data_df = pd.DataFrame(data_dict)

    stats = Statistics()
    stats.calculate(data_df, tuple(data_df.columns.to_list()))
    assert stats.mean_value("data1") == 1
    assert stats.mean_value("data2") == 22
    assert stats.mean_value("data3") == 333


def test_calculate_std():
    data_dict = dict(data1=[1, 1, 1, 1, 1],
                     data2=[22, 22, 22, 22, 22],
                     data3=[333, 333, 333, 333, 333])
    data_df = pd.DataFrame(data_dict)

    stats = Statistics()
    stats.calculate(data_df, tuple(data_df.columns.to_list()))
    assert stats.std_dev_value("data1") == 0
    assert stats.std_dev_value("data2") == 0
    assert stats.std_dev_value("data3") == 0
