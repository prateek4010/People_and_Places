APP_DIR := app
TEST_DIR := tests

build:
	docker-compose build

run:
	docker-compose up

run-app:
	docker-compose up $(APP_DIR)

run-tests:
	docker-compose up $(TEST_DIR)

stop-services:
	docker-compose down --remove-orphans