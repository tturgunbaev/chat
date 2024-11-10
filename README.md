# App to run langgraph server locally

## Requirements'
Set .env file with the following content:
```
OPENAI_API_KEY='openai-api-key'
LANGCHAIN_TRACING_V2=true
LANGSMITH_API_KEY='langsmith-api-key'
```

## Run steps
```
langgraph build -t my-image
export IMAGE_NAME=my-image
docker compose up -d
```