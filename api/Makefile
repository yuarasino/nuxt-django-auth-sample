.PHONY: manage runserver migrate createsuperuser test test-lf lint fmt


manage:
	venv/bin/python src/manage.py ${c}


runserver:
	@make manage c="runserver 0.0.0.0:8000"


migrate:
	@make manage c="migrate"


createsuperuser:
	@make manage c="createsuperuser"


test:
	venv/bin/pytest tests

test-lf:
	venv/bin/pytest --lf tests

lint:
	venv/bin/flake8 .
	venv/bin/mypy .

fmt:
	venv/bin/black .
	venv/bin/isort -y -rc .
