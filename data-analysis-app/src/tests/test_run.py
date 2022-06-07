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

from src.data_analysis_app.nodes import (
    get_data_for_mapping,
    get_data_from_xls_output_file,
    get_mapped_data,
    get_raw_data,
    save_mapped_data_to_xls,
)
from src.tests import data_for_testing

from src.data_analysis_app.pipeline_registry import register_pipelines


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
    data_for_mapping = pd.read_excel(
        "./src/tests/testing_data/mapping_for_testing.xlsx", engine="openpyxl"
    )

    return data_for_mapping


@pytest.fixture(scope="module")
def catalog_data():
    raw_data = pd.read_excel(
        "./src/tests/testing_data/data_for_testing.xlsx", engine="openpyxl"
    )

    return raw_data


@pytest.fixture(scope="module")
def catalog_read_output_data():
    raw_data_from_output = pd.read_excel(
        "./src/tests/testing_data/output_for_testing.xlsx", engine="openpyxl"
    )

    return raw_data_from_output


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


def test_data_for_raw_data(catalog_data):
    test_call_func = get_raw_data(catalog_data)

    test_for_not_empty_value = test_call_func.empty
    test_value = str(test_call_func.columns)
    test_count_of_header = test_call_func.shape[1]
    assert test_count_of_header == 5
    assert test_value == data_for_testing.LIST_OF_COLUMNS
    assert type(test_call_func) is pd.DataFrame
    assert test_for_not_empty_value is False


def test_get_mapped_data(catalog_mapping, catalog_data):
    """
    Tests the data is mapped according to the dict mapping

    :param catalog_mapping: get dict for mapping from test data
    :param catalog_data: get data from test data
    :return: mapped data
    """
    # get dict for mapping
    test_call_func_for_dict_mapping = get_data_for_mapping(catalog_mapping)
    # get data
    test_call_func_for_raw_data = get_raw_data(catalog_data)
    # count numbers of the row in the start
    count_of_row_start = test_call_func_for_raw_data.shape[0]

    # create mapped data
    test_call_func_for_test = get_mapped_data(
        test_call_func_for_dict_mapping, test_call_func_for_raw_data
    )
    # count rows after mapping has been done
    count_row = test_call_func_for_test.shape[0]

    test_for_not_empty_value = test_call_func_for_test.empty

    test_value = str(test_call_func_for_test.columns)

    test_count_of_header = test_call_func_for_test.shape[1]
    assert test_for_not_empty_value is False
    assert type(test_call_func_for_test) is pd.DataFrame
    assert test_count_of_header == 5
    assert test_value == data_for_testing.LIST_OF_COLUMNS_OUTPUT
    assert count_of_row_start == count_row


def test_for_raw_output_read_data(catalog_read_output_data):
    test_call_func = get_data_from_xls_output_file(catalog_read_output_data)

    test_for_not_empty_value = test_call_func.empty
    test_value = str(test_call_func.columns)
    test_count_of_header = test_call_func.shape[1]
    assert test_count_of_header == 5
    assert test_value == data_for_testing.LIST_OF_COLUMNS_OUTPUT
    assert type(test_call_func) is pd.DataFrame
    assert test_for_not_empty_value is False


def test_for_save_output_data(catalog_mapping, catalog_data, catalog_read_output_data):
    # get test data to create independent test
    test_call_func_for_dict_mapping = get_data_for_mapping(catalog_mapping)
    test_call_func_for_raw_data = get_raw_data(catalog_data)
    test_call_func_for_test_mapped_data = get_mapped_data(
        test_call_func_for_dict_mapping, test_call_func_for_raw_data
    )
    test_call_func_read_output_raw = get_data_from_xls_output_file(
        catalog_read_output_data
    )

    # call a test func/node
    test_func_for_saving = save_mapped_data_to_xls(
        test_call_func_for_test_mapped_data, test_call_func_read_output_raw
    )
    # counts rows in the start and in the end
    count_of_row_start = test_call_func_for_raw_data.shape[0]
    count_of_row_end_file = test_func_for_saving.shape[0]

    test_for_not_empty_value = test_func_for_saving.empty

    with pd.ExcelWriter(
            "./src/tests/testing_data/saved_output_for_testing.xlsx",
            mode="a",
            if_sheet_exists="replace",
    ) as writer:
        test_func_for_saving.to_excel(writer, float_format="%.3f", index=False)
    print(test_func_for_saving)

    test_value = str(test_func_for_saving.columns)
    test_count_of_header = test_func_for_saving.shape[1]
    assert test_count_of_header == 5
    assert test_value == data_for_testing.LIST_OF_COLUMNS_OUTPUT
    assert type(test_func_for_saving) is pd.DataFrame
    assert test_for_not_empty_value is False
    assert count_of_row_start == count_of_row_end_file


def test_registry_pipeline():
    test_call_func = register_pipelines()
    assert type(test_call_func) is dict
    assert test_call_func != {}
