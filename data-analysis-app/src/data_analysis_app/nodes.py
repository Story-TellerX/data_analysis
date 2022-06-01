"""
This is a boilerplate pipeline
generated using Kedro 0.18.1
"""

import logging
from typing import Dict

import pandas as pd


def get_data_for_mapping(data_for_mapping: pd.read_excel) -> Dict[str, str]:

    data_mapping = data_for_mapping

    dict_for_mapping = dict(data_mapping.iloc)

    return dict_for_mapping


def get_data(data_raw: pd.read_excel) -> pd.DataFrame:

    data_train = data_raw

    return data_train


def get_mapped_data(dict_for_mapping: Dict, data_train: pd.DataFrame) -> pd.DataFrame:

    mapped_data_to_xls_file = data_train.rename(dict_for_mapping, axis='columns')

    return mapped_data_to_xls_file