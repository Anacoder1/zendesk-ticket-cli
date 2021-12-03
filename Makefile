setup:
	@pipenv install

setup-dev:
	@pipenv install --dev

install:
	@python setup.py install

unit: setup-dev
	@py.test tests/unit/test_*.py

test: unit

lint: setup-dev
	black --line-length=80 ./