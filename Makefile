check-pip-env:
ifndef PIPENV_ACTIVE
	$(error Please activate pipenv using "pipenv shell")
endif

run: check-pip-env
	python -m patterns

test: check-pip-env
