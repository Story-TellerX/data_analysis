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
from kedro.framework.context import KedroContext
from kedro.framework.hooks import _create_hook_manager
from kedro.framework.project import settings

from src.data_analysis_app.nodes import get_data_for_mapping, get_raw_data
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
def catalog_mapping():
    data_for_mapping = pd.read_excel("./src/tests/testing_data/mapping_for_testing.xlsx", engine="openpyxl")

    return data_for_mapping


@pytest.fixture(scope="module")
def catalog_data():
    raw_data = pd.read_excel("./src/tests/testing_data/data_for_testing.xlsx", engine="openpyxl")

    return raw_data


# The tests below are here for the demonstration purpose
# and should be replaced with the ones testing the project
# functionality
class TestProjectContext:
    def test_project_path(self, project_context):
        assert project_context.project_path == Path.cwd()


def test_dict_for_mapping(catalog_mapping):
    test_call_func = get_data_for_mapping(catalog_mapping)

    test_size = len(test_call_func)
    assert type(test_call_func) is dict
    assert test_size > 0
    assert test_call_func == data_for_testing.DICT_FOR_MAPPING_TEST


def test_dict_for_raw_data(catalog_data):
    test_call_func = get_raw_data(catalog_data)
    test_for_not_empty_value = test_call_func.empty
    test_value = str(test_call_func.columns)
    test_count_of_header = test_call_func.shape[1]
    assert test_count_of_header == 5
    assert test_value == data_for_testing.LIST_OF_COLUMNS
    assert type(test_call_func) is pd.DataFrame
    assert test_for_not_empty_value is False
