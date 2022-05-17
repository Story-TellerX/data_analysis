path := cd ./data-analysis-app

running:
	$(path) && kedro run

requirements:
	pipenv install -r requirements.txt

venv:
	pipenv --three

env:
	source kedro-env/bin/activate
