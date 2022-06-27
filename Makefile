path := cd ./data-analysis-app
pyrun := pipenv run
venv := .venv

run: install
	$(path) && $(pyrun) kedro run

run_params:
	$(path) && $(pyrun) kedro run --params input_xlsx_path:./data/01_raw/data.xlsx,output_xlsx_path:./data/08_reporting/output.xlsx

test:
	$(path) && $(pyrun) kedro test

install: $(venv)
$(venv): $(venv)/bin/activate
$(venv)/bin/activate: Pipfile.lock
	$(call log, "Installing dependencies ...")
	pipenv --version &> /dev/null || pip install pipenv
	PIPENV_VENV_IN_PROJECT=1 pipenv install --dev
	touch $(venv)/bin/activate
	$(call log, "Installing dependencies Done")


rules :=	install				\
			run					\
			run_params			\
			test				\

.PHONY: $(rules)
.SILENT: $(rules) $(venv)/bin/activate
