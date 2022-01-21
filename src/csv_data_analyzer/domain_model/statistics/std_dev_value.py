# coding: utf-8

"""
StdDevValue class

Calculate standard deviation value of given array

Author: Shisato Yano
"""

import numpy as np


class StdDevValue:
    def calculate(self, array):
        return np.std(array)
