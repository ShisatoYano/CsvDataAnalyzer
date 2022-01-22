# coding: utf-8

"""
FileReader class

Ahthor: Shisato Yano
"""

import pandas as pd


class FileReader:
    def __init__(self, file_path):
        self._data_frame = pd.read_csv(file_path)

    def data_frame(self):
        data_frame_copy = self._data_frame.copy(deep=True)
        return data_frame_copy

    def data_name_list(self):
        return tuple(self._data_frame.columns.to_list())
