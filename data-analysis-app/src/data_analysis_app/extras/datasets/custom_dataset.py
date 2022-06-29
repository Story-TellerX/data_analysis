import os.path
from typing import Any, Dict
from pathlib import Path, PurePosixPath

import pandas as pd

from kedro.io import AbstractDataSet


class CustomDatSet(AbstractDataSet):
    """
    ``CustomDataSet`` loads / save csv / xlsx data from a given filepath as `pandas` DtaFrame using pd.read.
    """

    def __init__(self, filepath, path_to_file):
        """Creates a new instance of CustomDataSet to load / save xlsx / csv data at the given filepath.

        Args:
            filepath: The location of the xlsx / csv file to load / save data.
        """
        self._filepath = filepath
        self._filepath_to_xls = []
        self._filepath_to_csv = filepath
        for path in self._filepath:
            if Path(path).suffix == ".xlsx":
                self._filepath_to_xls = PurePosixPath(path)
            elif Path(path).suffix == ".csv":
                self._filepath_to_csv = PurePosixPath(path)
            else:
                raise TypeError

    def _load(self) -> dict:
        """Loads data from the xlsx / csv file.

        Returns:
            Data from the xls /csv file as a pandas DataFrame.
        """
        returned_data = {}
        for path in self._filepath:
            if Path(path).exists() and Path(path).suffix == ".xlsx":
                self._filepath_to_xls = PurePosixPath(path)
                data_from_file = pd.read_excel(self._filepath_to_xls, engine="openpyxl", convert_float=False)
                dict_from_file = {'xlsx': data_from_file}
                returned_data.update(dict_from_file)
            elif Path(path).exists() and Path(path).suffix == ".csv":
                self._filepath_to_csv = PurePosixPath(path)
                data_from_file = pd.read_csv(self._filepath_to_csv)
                dict_from_file = {'csv': data_from_file}
                returned_data.update(dict_from_file)
            elif not Path(path).exists():
                data_from_file = None
                dict_from_file = {'none': data_from_file}
                returned_data.update(dict_from_file)
            else:
                raise TypeError
        return returned_data


        # load_path_xlsx = self._filepath_to_xls
        # load_path_csv = self._filepath_to_csv
        # if Path(self._filepath_to_xls.as_posix()).exists():
        #     file_data_xlsx = pd.read_excel(load_path_xlsx, engine="openpyxl", convert_float=False)
        #     return file_data_xlsx
        # elif Path(self._filepath_to_csv.as_posix()).exists():
        #     file_data_csv = pd.read_csv(load_path_csv)
        #     return file_data_csv
        # else:
        #     raise IOError

    def _save(self, data: pd.DataFrame) -> None:
        """Saves file data to the specified filepath"""
        ...

    def _exists(self) -> bool:
        if Path(self._filepath.as_posix()).exists():
            return True
        elif Path(self._filepath_to_xls.as_posix()).exists():
            return True
        return False

    def _describe(self) -> Dict[str, Any]:
        """Returns a dict that describes the attributes of the dataset"""
        return dict(path_to_file=self._filepath_to_xls)
