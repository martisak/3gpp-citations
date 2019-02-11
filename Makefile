init:
	pip install -r requirements.txt

test: clean-pyc
	py.test --doctest-modules --pep8 standardcitations -v --cov standardcitations --cov-report term-missing

clean-pyc:
	-find . -name '*.pyc' -exec rm -f {} +
	-find . -name '*.pyo' -exec rm -f {} +

clean-build:
	-rm -rf build/
	-rm -rf dist/
	-rm -rf *.egg-info

build:
	python setup.py sdist bdist_wheel

.PHONY: init test clean-pyc clean-build
