.PHONY: lint
lint:
	poetry run flake8

.PHONY: run-llm
run-llm:
	poetry run python llm/main.py

.PHONY: api-test
api-test:
	curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8080/v1/chat/completions -d '{"context": "Chandrayaan-3 launched at 14 July 2023 and landed to south pole of moon at 23 August 2023.", "question":"When did Chandrayaan-3 landed?"}' | jq
