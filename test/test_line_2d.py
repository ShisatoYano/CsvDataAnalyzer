# coding: utf-8

"""
Test code for Line2D class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.visualization.line_2d import Line2D


def test_line_2d_plot():
    line_2d = Line2D()
    assert line_2d.plot([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], "red") is True
    assert line_2d.plot([1, 2, 3, 4, 5], [6, 7, 8], "red") is False
