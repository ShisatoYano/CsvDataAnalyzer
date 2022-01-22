# coding: utf-8

"""
CsvFile class

Author: Shisato Yano
"""


class CsvFile:
    def __init__(self, file_path):
        self._file_path = file_path

    def file_path(self):
        if self._is_readable(): return self._file_path
        return ""

    def _is_readable(self):
        if ".csv" in self._file_path: return True
        return False
