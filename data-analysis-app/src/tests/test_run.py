"""
This module contains an example test.

Tests should be placed in ``src/tests``, in modules that mirror your
project's structure, and in files named test_*.py. They are simply functions
named ``test_*`` which test a unit of logic.

To run the tests, run ``kedro test`` from the project root directory.
"""
from pathlib import Path

import pandas as pd
import pytest
from kedro.config import ConfigLoader
from kedro.extras.datasets.pandas import ExcelDataSet
from kedro.framework.context import KedroContext
from kedro.framework.hooks import _create_hook_manager
from kedro.framework.project import settings
from kedro.io import DataCatalog

from src.data_analysis_app.nodes import get_data_for_mapping
from src.tests import data_for_testing


@pytest.fixture
def config_loader():
    return ConfigLoader(conf_source=str(Path.cwd() / settings.CONF_SOURCE))


@pytest.fixture
def project_context(config_loader):
    return KedroContext(
        package_name="data_analysis_app",
        project_path=Path.cwd(),
        config_loader=config_loader,
        hook_manager=_create_hook_manager(),
    )


@pytest.fixture(scope="module")
def catalog():
    data_for_mapping = pd.read_excel("./data/01_raw/mapping.xlsx", engine="openpyxl")

    return data_for_mapping


# The tests below are here for the demonstration purpose
# and should be replaced with the ones testing the project
# functionality
class TestProjectContext:
    def test_project_path(self, project_context):
        assert project_context.project_path == Path.cwd()


def test_dict_for_mapping(catalog):
    print(catalog)
    test_call_func = get_data_for_mapping(catalog)
    assert test_call_func == data_for_testing.DICT_FOR_MAPPING_TEST
