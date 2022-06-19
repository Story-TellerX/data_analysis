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
        self._filepath = PurePosixPath(filepath)
        self._filepath_to_xls = PurePosixPath(path_to_file)

    def _load(self) -> pd.DataFrame:
        """Loads data from the xlsx / csv file.

        Returns:
            Data from the xls /csv file as a pandas DataFrame.
        """
        load_path_csv = self._filepath
        load_path_xlsx = self._filepath_to_xls
        if Path(self._filepath_to_xls.as_posix()).exists():
            file_data_xlsx = pd.read_excel(load_path_xlsx, engine="openpyxl", convert_float=False)
            return file_data_xlsx
        elif Path(self._filepath.as_posix()).exists():
            print(os.path.basename(load_path_csv))
            file_data_csv = pd.read_csv(load_path_csv)
            return file_data_csv
        else:
            raise IOError

    def _save(self, data: pd.DataFrame) -> None:
        """Saves file data to the specified filepath"""
        ...

    def _exists(self) -> bool:
        if Path(self._filepath.as_posix()).exists():
            return Path(self._filepath.as_posix()).exists()
        elif Path(self._filepath_to_xls.as_posix()).exists():
            return Path(self._filepath_to_xls.as_posix()).exists()

    def _describe(self) -> Dict[str, Any]:
        """Returns a dict that describes the attributes of the dataset"""
        return dict(path_to_file=self._filepath_to_xls)
