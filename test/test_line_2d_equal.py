# coding: utf-8

"""
Test code for Line2DEqual class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.visualization.line_2d_equal import Line2DEqual


def test_line_2d_equal_plot():
    line_2d_equal = Line2DEqual()
    assert line_2d_equal.plot([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], "red") is True
    assert line_2d_equal.plot([1, 2, 3, 4, 5], [6, 7, 8], "red") is False
