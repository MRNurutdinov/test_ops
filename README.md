# Tes Sberbank XOps

Для накатывания миграций, терминале команды:

- ```pip install -r requirements.txt ```
- docker-compose up --build
- Дальше вводим: ```alembic upgrade heads``

Терепь можно запустить тесты
-- pytest tests/

После тестов запускаем проект
-- uvicorn main.py:app --reload

По ссылке http://127.0.0.1:8000/docs будут реализованы все методы
