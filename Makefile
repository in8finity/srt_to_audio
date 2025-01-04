.PHONY: run
run: dev.build
	docker-compose -f ./docker-compose-dev.yml --env-file ./env.dev run app converter

.PHONY: dev.back.console
dev.back.console: dev.up
	echo "Starting shell in app container..."
	docker-compose -f ./docker-compose-dev.yml --env-file ./env.dev exec -it app bash 

.PHONY: dev.up
dev.up:
	echo "Starting app containers..."
	docker-compose -f ./docker-compose-dev.yml --env-file ./env.dev up -d

.PHONY: dev.down
dev.down:
	echo "Stopping app containers..."
	docker-compose -f ./docker-compose-dev.yml --env-file ./env.dev down

.PHONY: dev.build
dev.build:
	echo "Building app containers..."
	docker-compose -f ./docker-compose-dev.yml --env-file ./env.dev build