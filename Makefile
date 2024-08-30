install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

#checks python files
lint:
	pylint --ignore-patterns = test_main.py

test:
	python -m pytest -cov=main test_main.py

all: 
	install format lint test