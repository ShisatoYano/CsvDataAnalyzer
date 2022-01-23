# coding: utf-8

"""
Test code for Heatmap2D class

Author: Shisato Yano
"""


import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.visualization.heatmap_2d import Heatmap2D


def test_heatmap_2d_plot():
    heatmap_2d = Heatmap2D()
    assert heatmap_2d.plot([1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                           [3, 4, 10, 0, 7], 0, 10) is True
    assert heatmap_2d.plot([1, 2, 3, 4, 5], [6, 7, 8],
                           [3, 4, 10, 0, 7], 0, 10) is False
