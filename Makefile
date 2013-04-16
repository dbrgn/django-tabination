.PHONY: help install flake8 test report report-html clean

help:
	@echo "The purpose of this Makefile is to help testing django-tabination."
	@echo
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  install        to install all packages required for testing"
	@echo "  flake8         to run flake8"
	@echo "  test           to run the test suite"
	@echo "  report         to generate a coverage report"
	@echo "  report-html    to generate and open a HTML coverage report"
	@echo "  clean          to clean up coverage results"

install:
	pip install -U -r requirements/tests.txt
	pip install -U -e .
	@echo "Please don't forget to run 'pip install Django'"

flake8:
	flake8 tabination --ignore=E128 --max-line-length=99

test:
	coverage run --branch --source=tabination `which django-admin.py` test --settings=tabination.test_settings tabination

report: flake8 test
	coverage report

report-html: flake8 test
	coverage html
	@python -c "import os, webbrowser; webbrowser.open('file://%s/htmlcov/index.html' % os.getcwd())"

clean:
	rm -f .coverage
	rm -rf htmlcov
