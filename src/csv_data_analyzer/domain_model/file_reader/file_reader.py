# coding: utf-8

"""
FileReader class

Ahthor: Shisato Yano
"""

import pandas as pd

from ..csv_file.csv_file import CsvFile


class FileReader:
    def __init__(self):
        self._data_frame = None
        self._csv_file = CsvFile()

    def read_csv_file(self, file_path):
        if self._csv_file.is_readable(file_path):
            self._data_frame = pd.read_csv(file_path)

    def data_frame(self):
        return self._data_frame
