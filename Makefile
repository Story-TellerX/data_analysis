path := cd ./data-analysis-app

running:
	$(path) && kedro run

run_params:
	$(path) && kedro run --params output_csv_path:data/08_reporting/output.csv

requirements:
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv install -r

venv:
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv --three
