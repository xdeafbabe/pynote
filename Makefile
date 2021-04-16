.DEFAULT: help
.PHONY: help deps lint test testreport coverage outdated build clean

help:
	@echo "Please use '$(MAKE) <target>' where <target> is one of the following:"
	@echo "  help        - show help information"
	@echo "  deps        - install project dependencies"
	@echo "  lint        - inspect project source code for errors"
	@echo "  test        - run project tests"
	@echo "  testreport  - run project tests and open HTML coverage report"
	@echo "  coverage    - run project tests and save coverage to XML file"
	@echo "  outdated    - list outdated project requirements"
	@echo "  build       - build project package"
	@echo "  clean       - clean up project environment and build artifacts"

deps:
	python3 -m pip install pip==21.0.1 setuptools==54.2.0 wheel==0.36.2
	python3 -m pip install -e .[dev,test]

lint:
	python3 -m flake8 pynote tests

test:
	python3 -m pytest --cov-report=term-missing

testreport:
	python3 -m pytest --cov-report=html
	xdg-open htmlcov/index.html

coverage:
	python3 -m pytest --cov-report=xml

outdated:
	python3 -m pip list --outdated --format=columns

build:
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf *.egg .eggs *.egg-info .pytest_cache htmlcov .coverage .venv build dist
