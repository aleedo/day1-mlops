install:
	pip install -r requirements.txt

lint:
	pylint binary_search.py

test:
	python -m pytest -vv

deploy:
	uvicorn app:app