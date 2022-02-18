install:
	 poetry install
	 poetry run pip install scikit-learn==1.0.2

test:
	poetry run pytest -s --disable-warnings

build:
	rm -rf ./dist
	poetry export -f requirements.txt > requirements.txt
	poetry build

publish: build
	poetry publish

config:
	poetry config virtualenvs.create false --local
