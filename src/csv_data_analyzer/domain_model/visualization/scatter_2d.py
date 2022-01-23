# coding: utf-8

"""
Scatter2D class

Author: Shisato Yano
"""

import matplotlib.pyplot as plt


class Scatter2D:
    def __init__(self):
        self._fig, self._axes = plt.subplots()

    def plot(self, data_x, data_y, color, marker):
        if not self._is_same_size(data_x, data_y): return False
        self._axes.scatter(data_x, data_y, c=color, marker=marker, s=30)
        self._axes.grid(True)
        return True

    def _is_same_size(self, data_x, data_y):
        if len(data_x) == len(data_y): return True
        return False
