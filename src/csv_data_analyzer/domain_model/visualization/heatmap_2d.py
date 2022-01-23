# coding: utf-8

"""
Heatmap2D class

Author: Shisato Yano
"""

import matplotlib.pyplot as plt


class Heatmap2D:
    def __init__(self):
        self._fig, self._axes = plt.subplots()

    def plot(self, data_x, data_y, data_c,
             c_min, c_max):
        if not self._is_same_size(data_x, data_y): return False
        sc = self._axes.scatter(data_x, data_y, c=data_c, cmap="jet",
                                vmin=round(float(c_min), 1),
                                vmax=round(float(c_max), 1),
                                marker='.', s=30)
        self._axes.grid(True)
        plt.colorbar(sc)
        return True

    def _is_same_size(self, data_x, data_y):
        if len(data_x) == len(data_y): return True
        return False
