.PHONY: install test run

install:
	python3 -m pip install -e .[dev]

test:
	pytest

run:
	uvicorn openazv_goods_ecosystem.app:app --host 0.0.0.0 --port 8080
