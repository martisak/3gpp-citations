init:
	pip install -r requirements.txt

test:
	py.test --doctest-modules --pep8 standardcitations -v --cov standardcitations --cov-report term-missing

.PHONY: init test