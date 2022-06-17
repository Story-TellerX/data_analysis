"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from data_analysis_app.pipeline import (
    create_pipeline_for_mapping_and_write_xls,
    create_pipeline_for_csv_file,
)


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {
        "__default__": create_pipeline_for_mapping_and_write_xls(),
        "csv": create_pipeline_for_csv_file(),
    }
