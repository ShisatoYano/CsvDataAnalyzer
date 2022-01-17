# coding: utf-8

"""
Test code for User class

Author: Shisato Yano
"""

import sys
sys.path.append("../")

from src.csv_data_analyzer.domain_model.user.user import User

TEST_PATH_CUR_DIR = "sample.csv"
TEST_PATH_DATA_DIR = "data/sample.csv"
TEST_PATH_MULTI_DIR = "data1/data2/sample.csv"
TEST_PATH_NO_CSV = "sample.txt"


def test_init():
    user = User()
    assert "" == user.csv_file_path()


def test_select_csv_file():
    user_cur_dir = User()
    user_cur_dir.select_csv_file(TEST_PATH_CUR_DIR)
    assert TEST_PATH_CUR_DIR == user_cur_dir.csv_file_path()

    user_data_dir = User()
    user_data_dir.select_csv_file(TEST_PATH_DATA_DIR)
    assert TEST_PATH_DATA_DIR == user_data_dir.csv_file_path()

    user_multi_dir = User()
    user_multi_dir.select_csv_file(TEST_PATH_MULTI_DIR)
    assert TEST_PATH_MULTI_DIR == user_multi_dir.csv_file_path()


def test_csv_file_name():
    user_cur_dir = User()
    user_cur_dir.select_csv_file(TEST_PATH_CUR_DIR)
    assert "sample.csv" == user_cur_dir.csv_file_name()

    user_data_dir = User()
    user_data_dir.select_csv_file(TEST_PATH_DATA_DIR)
    assert "sample.csv" == user_data_dir.csv_file_name()

    user_multi_dir = User()
    user_multi_dir.select_csv_file(TEST_PATH_MULTI_DIR)
    assert "sample.csv" == user_multi_dir.csv_file_name()


def test_is_csv_file():
    user_csv = User()
    user_csv.select_csv_file(TEST_PATH_CUR_DIR)
    assert True is user_csv.is_csv_file()

    user_no_csv = User()
    user_no_csv.select_csv_file(TEST_PATH_NO_CSV)
    assert False is user_no_csv.is_csv_file()
