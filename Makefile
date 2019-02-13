init:
	pip install -r requirements.txt

test: clean-pyc
	py.test \
		--pylint --pylint-jobs=4  \
		--flakes --doctest-modules \
		--pep8 standardcitations -v \
		--cov standardcitations --cov-report term-missing \
		--durations=10

clean-pyc:
	-find . -name '*.pyc' -exec rm -f {} +
	-find . -name '*.pyo' -exec rm -f {} +

clean-build:
	-rm -rf build/
	-rm -rf dist/
	-rm -rf *.egg-info

lint:
	/usr/bin/env python `which pylint` standardcitations

build:
	python setup.py sdist bdist_wheel

.PHONY: init test clean-pyc clean-build
