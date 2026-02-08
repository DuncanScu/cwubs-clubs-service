.PHONY: dev, install

install:
	poetry install

dev:
	poetry run uvicorn app.main:app --reload
