# coding: utf-8

"""
Test code for Scatter2DEqual class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.visualization.scatter_2d_equal import Scatter2DEqual


def test_scatter_2d_equal_plot():
    scatter_2d_equal = Scatter2DEqual()
    assert scatter_2d_equal.plot([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], "red", "o") is True
    assert scatter_2d_equal.plot([1, 2, 3, 4, 5], [6, 7, 8], "red", "o") is False
