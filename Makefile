init:
	pip install -r requirements.txt

test:
	py.test

.PHONY: init test