DICT_FOR_MAPPING_TEST = {
    "Spend (SGD)": "SPEND",
    "Invoice no": "INVOICE_NO",
    "PO number": "DOC_NO",
    "Currency": "CURRENCY",
    "Invoice date": "INVOICE",
}

LIST_OF_COLUMNS = (
    "Index"
    "(['Invoice no', 'PO number', 'Currency', 'Invoice date', 'Spend (SGD)'],"
    " dtype='object')"
)

LIST_OF_COLUMNS_OUTPUT = (
    "Index(['INVOICE_NO', 'DOC_NO', 'CURRENCY', 'INVOICE', 'SPEND'], dtype='object')"
)

PIPELINE_CSV = "Pipeline([\n" \
               "Node(get_raw_data, ['data_raw_csv', 'data_raw_xlsx'], 'data_train', 'get_data_and_make_map'),\n" \
               "Node(create_csv_file_from_xlsx, ['data_train', 'params:inpath_to_created_csv'], 'raw_data_xlsx', 'raw_csv')\n" \
               "])"

LIST_OF_INPUT_DATES_CSV = [
    (0, '2019/01/14'),
    (1, '2019/01/03'),
    (2, '2019/01/22'),
    (3, '2019/01/07'),
    (4, '2019/01/21'),
    (5, '2019/10/09'),
    (6, '2019/10/24'),
    (7, '2019/10/24'),
    (8, '2019/10/10'),
    (9, '2019/10/04'),
    (10, '2019/10/17'),
    (11, '2019/01/03'),
    (12, '2019/01/16'),
    (13, '2019/01/01'),
    (14, '2019/02/25'),
    (15, '2019/02/06'),
    (16, '2019/02/26'),
    (17, '2019/02/08')
]

LIST_OF_OUTPUT_DATES = [
    (0, '20190114'),
    (1, '20190103'),
    (2, '20190122'),
    (3, '20190107'),
    (4, '20190121'),
    (5, '20191009'),
    (6, '20191024'),
    (7, '20191024'),
    (8, '20191010'),
    (9, '20191004'),
    (10, '20191017'),
    (11, '20190103'),
    (12, '20190116'),
    (13, '20190101'),
    (14, '20190225'),
    (15, '20190206'),
    (16, '20190226'),
    (17, '20190208')
]

