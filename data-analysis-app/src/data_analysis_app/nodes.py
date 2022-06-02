"""
This is a boilerplate pipeline
generated using Kedro 0.18.1
"""
import os
import logging
from typing import Dict
import zipfile

import pandas as pd
from kedro.extras.datasets.pandas import ExcelDataSet


def get_data_for_mapping(data_for_mapping: pd.read_excel) -> Dict[str, str]:
    """Uses pandas read ExcelDataSet for getting data for mapping as headers.

    Args:
        data_for_mapping: Training data of mapping.

    Returns:
        dict_for_mapping: Dict of the target headers.
    """

    data_mapping = data_for_mapping

    dict_for_mapping = dict(data_mapping.iloc)

    return dict_for_mapping


def get_data(data_raw: pd.read_excel) -> pd.DataFrame:
    """Uses pandas read ExcelDataSet for getting training data.

    Args:
        data_raw: Training data.

    Returns:
        pandas DataFrame.
    """

    data_train = data_raw

    return data_train


def get_mapped_data(dict_for_mapping: Dict, data_train: pd.DataFrame) -> pd.DataFrame:
    """Uses pandas read ExcelDataSet for getting training data.

    Args:
        data_train: Training data.
        dict_for_mapping: Dict of the target headers

    Returns:
        pandas DataFrame: mapped data.
    """

    mapped_data_to_xls_file = data_train.rename(dict_for_mapping, axis='columns')

    return mapped_data_to_xls_file


def save_mapped_data_to_xls(mapped_data_to_xls_file: pd.DataFrame, mapped_data) -> None:
    """Uses pandas read to_excel for save training mapped data.

    Args:
        mapped_data_to_xls_file: Training mapped data.
        mapped_data: structure of exists xlsx file where will be saved data

    Returns:
        None
    """

    filepath_to_file = _filepath_to_output_file()

    data_set = ExcelDataSet(filepath=filepath_to_file)
    data_set.save(mapped_data_to_xls_file)

    filename = filepath_to_file

    with zipfile.ZipFile("output_data.zip", mode="w") as archive:
        archive.write(filename)


def _filepath_to_output_file() -> str:
    """Uses os module to get absolute path to output xlsx file.

    Returns:
        Path to file as str
    """

    exe = 'output.xlsx'
    filepath_to_file_raw = ''
    for root, dirs, files in os.walk(r"/app"):
        for name in files:
            if name == exe:
                filepath_to_file_raw = os.path.abspath(os.path.join(root, name))
                return filepath_to_file_raw
