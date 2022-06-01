"""
This is a boilerplate pipeline
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import get_data_for_mapping, get_data


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
                inputs=["data_raw", "dict_for_mapping"],
                outputs="data_train",
                name="get_data_and_make_map",
            ),
            # node(
            #     func=report_accuracy,
            #     inputs=["y_pred", "y_test"],
            #     outputs=None,
            #     name="report_accuracy",
            # ),
        ]
    )
