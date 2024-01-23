# Default task
.PHONY: help
help:
	@echo "Use 'make <target>' where <target> is one of:"
	@echo "  install       	 - Install dependencies"
	@echo "  makemigrations	 - Create database migrations"
	@echo "  migrate       	 - Apply database migrations"
	@echo "  runserver     	 - Run the development server"
	@echo "  createsuperuser 	 - Create a superuser for the admin panel"

install:
	pip install -r requirements.txt

makemigrations:
	python NAG/manage.py makemigrations --settings=NAG.local_settings

migrate:
	python NAG/manage.py migrate --settings=NAG.local_settings

runserver:
	python NAG/manage.py runserver --settings=NAG.local_settings

createsuperuser:
	python NAG/manage.py createsuperuser --settings=NAG.local_settings
