.PHONY: manage runserver migrate createsuperuser


manage:
	venv/bin/python src/manage.py ${c}


runserver:
	@make manage c="runserver 0.0.0.0:8000"


migrate:
	@make manage c="migrate"


createsuperuser:
	@make manage c="createsuperuser"
