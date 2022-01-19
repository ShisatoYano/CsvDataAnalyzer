# coding: utf-8

"""
CsvDataAnalyzer

GUI python tool for analyzing CSV data.

Author: Shisato Yano
"""

import argparse

from domain_model import *


def main():
    # generate ArgumentParser object
    parser = argparse.ArgumentParser()

    # setting command line option
    # csv file path as string
    parser.add_argument("-f", "--file", help="CSV file path",
                        type=str, default="")

    # get and analyze command line input
    args = parser.parse_args()

    # User select a file
    user_obj = User()
    user_obj.select_file(args.file)

    # Read selected file
    reader = FileReader()
    reader.read_csv_file(user_obj.file_path())
    print(reader.data_frame())


if __name__ == "__main__":
    main()
