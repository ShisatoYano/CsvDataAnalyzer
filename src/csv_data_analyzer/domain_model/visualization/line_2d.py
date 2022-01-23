# coding: utf-8

"""
Line2D class

Author: Shisato Yano
"""

import matplotlib.pyplot as plt


class Line2D:
    def __init__(self):
        self.fig, self.axes = plt.subplots()

    def plot(self, data_x, data_y, color):
        if not self._is_same_size(data_x, data_y): return False
        self.axes.plot(data_x, data_y, c=color,
                       linestyle="solid", linewidth=3)
        self.axes.grid(True)
        return True

    def _is_same_size(self, data_x, data_y):
        if len(data_x) == len(data_y): return True
        return False
