"""
This is a boilerplate pipeline
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    get_data_for_mapping,
    get_data,
    get_mapped_data,
    save_mapped_data_to_xls,
    get_data_from_xls_output_file
)


def create_pipeline_for_mapping_and_write_xls(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=get_data_for_mapping,
                inputs=["data_for_mapping"],
                outputs="dict_for_mapping",
                name="get_dict_for_mapping",
            ),
            node(
                func=get_data,
                inputs=["data_raw"],
                outputs="data_train",
                name="get_data_and_make_map",
            ),
            node(
                func=get_mapped_data,
                inputs=["dict_for_mapping", "data_train"],
                outputs="mapped_data_to_xls_file",
                name="mapped_data",
            ),
            node(
                func=get_data_from_xls_output_file,
                inputs="mapped_data",
                outputs="mapped_empty_data_as_dataframe",
                name="raw_output_xls_file",
            ),
            node(
                func=save_mapped_data_to_xls,
                inputs=["mapped_data_to_xls_file", "mapped_empty_data_as_dataframe"],
                outputs="save_mapped_data",  # should be return mapped data
                name="_output_xls_file",
            ),
        ]
    )
