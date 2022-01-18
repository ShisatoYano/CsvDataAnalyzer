# coding: utf-8

"""
User class

This class know the following information.

Path to file you want to read.
Name of file.

Author: Shisato Yano
"""


class User:
    def __init__(self):
        self._file_path = ""

    def select_file(self, file_path):
        self._file_path = file_path

    def file_name(self):
        return self._file_path.split('/')[-1]

    def file_path(self):
        return self._file_path
