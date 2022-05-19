path := cd ./data-analysis-app

running:
	$(path) && kedro run

requirements:
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv install -r

venv:
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv --three
