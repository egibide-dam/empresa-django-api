#!make

help: _header
	${info }
	@echo Opciones:
	@echo ----------------------
	@echo build
	@echo start / stop / restart
	@echo workspace
	@echo clean
	@echo ----------------------

_header:
	@echo ----------
	@echo Django API
	@echo ----------

_urls:
	${info }
	@echo ----------------------------------------
	@echo [Swagger] http://localhost:8000/swagger/
	@echo ----------------------------------------

build:
	@docker compose build --pull

_start-command:
	@docker compose up -d

start: _start-command _urls

stop:
	@docker compose stop

restart: stop start

workspace:
	@docker compose exec django /bin/bash

clean:
	@docker compose down -v --remove-orphans
