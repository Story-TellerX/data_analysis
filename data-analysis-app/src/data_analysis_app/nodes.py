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


def get_data(data_raw: pd.read_excel):

    data_train = data_raw

    return data_train
