# coding: utf-8

"""
CsvDataAnalyzer

GUI python tool for analyzing CSV data.

Author: Shisato Yano
"""

import argparse
import os.path

from domain_model.user.user import User


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
    user = User()
    user.select_file(args.file)


if __name__ == "__main__":
    main()
