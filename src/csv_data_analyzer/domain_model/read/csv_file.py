# coding: utf-8

"""
CsvFile class

Author: Shisato Yano
"""


class CsvFile:
    def __init__(self, path):
        self._path = path

    def path(self):
        return self._path

    def is_readable(self):
        if ".csv" in self._path: return True
        return False
