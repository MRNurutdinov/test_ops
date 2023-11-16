# Tes Sberbank XOps

Для накатывания миграций, терминале команды:

- ```pip install -r requirements.txt ```
- docker-compose up --build
- Дальше вводим: ```alembic upgrade heads``
-- uvicorn  main.py:app --reload