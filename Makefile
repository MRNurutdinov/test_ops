up:
	docker compose -f docker-compose.yaml up -d

pip-install:
     pip install -r requirements.txt

migrations:
    alembic upgrade heads

down:
    docker-compose -f docker-compose.yaml down && docker network prune --force
