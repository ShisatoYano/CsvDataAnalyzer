# coding: utf-8

"""
CsvFile class

Author: Shisato Yano
"""


class CsvFile:
    def is_csv_file(self, file_path):
        if ".csv" in file_path:
            return True
        else:
            return False