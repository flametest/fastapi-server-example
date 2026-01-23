check:
	pre-commit run --all-files
docker:
	docker build -t fastapi-server-example:0.1.2 .
