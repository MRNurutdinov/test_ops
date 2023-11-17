from httpx import AsyncClient

"""
Тестируем API по работе с историями пользователя
"""


async def test_add_hisory_user_success(ac: AsyncClient):
    response = await ac.post("/visited_links", json={
        "links": [
            "yandex.ru",
            "yandex.ru/web",
            "yandex.ru",
            "sberbank.ru",
        ]
    })

    assert response.status_code == 200

async def test_add_user_history_empty_list(ac: AsyncClient):
    # Создаем тестовые данные с пустым списком ссылок
    data = {
        "links": []
    }

    # Отправляем POST-запрос
    response = await ac.post("/visited_links", json=data)

    # Проверяем статус код и ожидаемый результат
    assert response.status_code == 400
    assert response.json() == {"detail": "Пустой список"}


async def test_add_user_history_number_list(ac: AsyncClient):
    # Создаем тестовые данные с пустым списком ссылок
    data = {
        "links": [123, True, 7.0, (1, 2, 3)]
    }

    # Отправляем POST-запрос
    response = await ac.post("/visited_links", json=data)

    # Проверяем статус код и ожидаемый результат
    assert response.status_code == 400
    assert response.json() == {"detail": "Некорректный формат данных. Ожидается список строк."}


async def test_add_user_history_invalid_data(ac: AsyncClient):
    # Создаем тестовые данные с неверным форматом
    data = {
        "links": "https://example.com"
    }

    # Отправляем POST-запрос
    response = await ac.post("/visited_links", json=data)

    # Проверяем статус код и ожидаемый результат
    assert response.status_code == 422
