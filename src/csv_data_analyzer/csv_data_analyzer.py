# coding: utf-8

"""
CsvDataAnalyzer

GUI python tool for analyzing CSV data.

Author: Shisato Yano
"""

import argparse
import matplotlib.pyplot as plt

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

    # select a file
    csv_object = CsvFile(args.file)

    # Read selected file
    reader = FileReader(csv_object.file_path())

    # Calculate statistics
    stats = Statistics()
    stats.calculate(reader.data_frame(), reader.data_name_list())

    # Plot data graph
    l2d = Line2D()
    l2d.plot(reader.data_array("pointNum"),
             reader.data_array("player1Score"),
             "red")
    l2de = Line2DEqual()
    l2de.plot(reader.data_array("pointNum"),
              reader.data_array("player1Score"),
              "red")
    sc2d = Scatter2D()
    sc2d.plot(reader.data_array("pointNum"),
              reader.data_array("player1Score"),
              "blue", "*")
    sc2de = Scatter2DEqual()
    sc2de.plot(reader.data_array("pointNum"),
               reader.data_array("player1Score"),
               "blue", "*")
    hm2d = Heatmap2D()
    hm2d.plot(reader.data_array("pointNum"),
              reader.data_array("player1Score"),
              reader.data_array("pointNum"),
              min(reader.data_array("pointNum")),
              max(reader.data_array("pointNum")))
    hm2de = Heatmap2DEqual()
    hm2de.plot(reader.data_array("pointNum"),
               reader.data_array("player1Score"),
               reader.data_array("pointNum"),
               min(reader.data_array("pointNum")),
               max(reader.data_array("pointNum")))

    plt.show()


if __name__ == "__main__":
    main()
