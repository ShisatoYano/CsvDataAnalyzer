# coding: utf-8

"""
CsvDataAnalyzer

GUI python tool for analyzing CSV data.

Author: Shisato Yano
"""

import argparse
import os.path


def main():
    # generate ArgumentParser object
    parser = argparse.ArgumentParser()

    # setting command line option
    # csv file path as string
    parser.add_argument("-f", "--file", help="CSV file path",
                        type=str, default="")

    # get and analyze command line input
    args = parser.parse_args()
    print(os.path.exists(args.file))


if __name__ == "__main__":
    main()
