# insightsGPT

Application for scanning RHEL systems (also insights-report/sosreports), diagnosing and triaging issues in simple english. With the help of Red Hat’s knowledge base(KCS)  + the power of LLM(Large language model) pulls out the relevant information and provides resolution.

Service can integrate with pre existing tools like insights-client, sos(sosreport) etc.


## Architecture Diagram


![](./docs/images/architecture-diagram.jpg)


## Installation

We use poetry for dependency management so make sure that poetry binary is installed - [doc](https://python-poetry.org/docs/).

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Install the needed dependencies. 

```bash
poetry install
```

To start cromadb(where all the KCS will be embedded and stored) use the below command. 

```
podman-compose up
```

Start llm service using below. 
```
make run-llm 
```

Start insightsGPT-backend service using below. 
```
make run-backend
```

## Usage

There is load_data.py script which loads the KCS article from the docs/kcs directory and store them in the cromaDB. 
```
poetry run python load_data.py
```

Use below make target to trigger test API. 

```
make api-test
```


llm service has a `/completions` endpoint where one can pass the context and ask the related question to llm model.  

```
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8080/v1/chat/completions -d '{"context": "Chandrayaan-3 launched at 14 July 2023 and landed to south pole of moon at 23 August 2023.", "question":"When did Chandrayaan-3 landed?"}' | jq
```
