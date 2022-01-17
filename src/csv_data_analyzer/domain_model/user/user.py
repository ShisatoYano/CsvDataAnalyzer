# coding: utf-8

"""
User class

This class know the following information.

Path to CSV file you want to read.
Name of CSV file.
Directory the CSV file is located.

Author: Shisato Yano
"""


class User:
    def __init__(self):
        self.file_path = ""

    def select_csv_file(self, csv_file_path):
        self.file_path = csv_file_path

    def csv_file_name(self):
        return self.file_path.split('/')[-1]

    def csv_file_path(self):
        return self.file_path

    def is_csv_file(self):
        return ".csv" in self.file_path.split('/')[-1]
