"""
This is a boilerplate pipeline
generated using Kedro 0.18.1
"""
import os
import zipfile
from typing import Dict

import pandas as pd
from kedro.io import IncrementalDataSet


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


def get_raw_data(data_raw) -> pd.DataFrame:
    """Uses pandas read ExcelDataSet for getting training data.

    Args:
        data_raw: Training data from xlsx or csv file.

    Returns:
        pandas DataFrame.
    """

    # if data_raw_csv != {} and data_raw_xlsx != {}:
    #     data_train = data_raw_xlsx
    #     return data_train
    # elif data_raw_xlsx:
    #     data_train = data_raw_xlsx
    #     return data_train
    # if data_raw_csv:
    # data_train = data_raw
    # return data_train
    # else:
    #     raise ValueError
    # data_train['Invoice date'] = pd.to_datetime(data_train['Invoice date']).dt.strftime("%Y/%m/%d")

    if data_raw['xlsx'] is not None:
        data_train = data_raw['xlsx']
    elif data_raw['csv'] is not None:
        data_train = data_raw['csv']
    else:
        raise ValueError
    return data_train


def get_mapped_data(dict_for_mapping: Dict, data_train_format: pd.DataFrame) -> pd.DataFrame:
    """Uses pandas read ExcelDataSet for getting training data.

    Args:
        data_train_format: Training data.
        dict_for_mapping: Dict of the target headers

    Returns:
        pandas DataFrame: mapped data.

    """

    mapped_data_to_xls_file = data_train_format.rename(dict_for_mapping, axis="columns")

    return mapped_data_to_xls_file


def get_data_from_xls_output_file(output_xlsx_path) -> pd.DataFrame:
    """Uses pandas read to_excel for get DataFrames from empty output xlsx file.

    Args:
        output_xlsx_path: read structure from output xlsx file to get DataFrames.

    Returns:
        mapped_empty_data_as_dataframe as pd.DataFrame
    """

    mapped_empty_data_as_dataframe = pd.read_excel(output_xlsx_path, engine="openpyxl", convert_float=False)

    return mapped_empty_data_as_dataframe


def save_mapped_data_to_xls(
        mapped_data_to_xls_file: pd.DataFrame, mapped_empty_data_as_dataframe: pd.DataFrame
) -> pd.DataFrame:
    """Uses pandas read to_excel for save training mapped data.

    Args:
        mapped_data_to_xls_file: Training mapped data.
        mapped_empty_data_as_dataframe: structure of xlsx file where will be saved data

    Returns:
        save_mapped_data as pd.DataFrame with call action to_excel from catalog yaml
    """
    mapped_data = mapped_empty_data_as_dataframe

    data_to_xls_file = mapped_data_to_xls_file

    mapped_data.drop(mapped_data.index, inplace=True)

    save_mapped_data = mapped_data.merge(data_to_xls_file, how="right")

    inpath_csv = "./data/08_reporting/output.csv"
    save_mapped_data.to_csv(inpath_csv, index=False)

    # Creating a zip file
    # Takes filepath to xlsx file
    # inpath = "./data/08_reporting/output.xlsx"
    # # put a path to output file
    # outpath = "./data/09_output/output_data_zip.zip"
    # with zipfile.ZipFile(outpath, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    #     # put two params to writer first - filepath to file which should be zipped,
    #     # second - filepath to dir where should be putted archived file
    #     archive.write(inpath, os.path.basename(inpath))

    # Create a zip for multiple files
    inpath = ["./data/08_reporting/output.xlsx", "./data/08_reporting/output.csv"]
    # put a path to output file
    outpath = "./data/09_output/output_data_zip.zip"
    with zipfile.ZipFile(outpath, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file in inpath:
            archive.write(file, os.path.basename(file))

    return save_mapped_data


# first solution for search filepath to xlsx file
# def _filepath_to_output_file() -> str:
#     """Uses os module to get absolute path to output xlsx file.
#
#     Returns:
#         Path to file as str
#     """
#
#     exe = 'output.xlsx'
#     filepath_to_file_raw = ''
#     for root, dirs, files in os.walk(r"/home"):
#         for name in files:
#             if name == exe:
#                 filepath_to_file_raw = os.path.abspath(os.path.join(root, name))
#                 return filepath_to_file_raw


def create_csv_file_from_xlsx(data_train: pd.DataFrame, inpath_to_created_csv) -> pd.DataFrame:
    raw_data_xlsx = data_train
    raw_data_xlsx['Invoice date'] = pd.to_datetime(raw_data_xlsx['Invoice date']).dt.strftime("%Y/%m/%d")
    raw_data_xlsx.to_csv(inpath_to_created_csv, index=False)
    return raw_data_xlsx


def parse_and_format_dates(data_train: pd.DataFrame) -> pd.DataFrame:
    data_train.loc[0:, "Invoice date"] = pd.to_datetime(data_train["Invoice date"]).dt.strftime("%Y%m%d")
    return data_train
