.PHONY: lint
lint:
	poetry run flake8

.PHONY: run-llm
run-llm:
	poetry run python llm/main.py