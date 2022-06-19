path := cd ./data-analysis-app

run:
	$(path) && kedro run

run_params:
	$(path) && kedro run --params input_xlsx_path:./data/01_raw/data.xlsx,output_xlsx_path:./data/08_reporting/output.xlsx

test:
	$(path) && kedro test

requirements:
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv install -r

venv:
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv --three
