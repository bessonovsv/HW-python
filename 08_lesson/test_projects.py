import pytest
from project_page import ProjectPage


@pytest.fixture(scope="module")
def project_page():
    return ProjectPage()


# Позитивные тесты
# Создание проекта
def test_create_project_success(project_page):
    project_data = {
        "title": "Домашнее задание API",
        "users": {
            "41041360-e041-4300-8eec-fd69f049f1c0": "worker"
        }
    }
    response = project_page.create_project(project_data)
    assert response.status_code == 201  # Ожидаем статус 201 Created
    assert 'id' in response.json()  # Проверяем, что проект создан и есть ID


# Изменение проекта
def test_update_project_success(project_page):
    # Сначала создаем проект для обновления
    project_data = {
        "title": "Домашнее задание API",
        "users": {
            "41041360-e041-4300-8eec-fd69f049f1c0": "worker"
        }
    }
    create_response = project_page.create_project(project_data)
    project_id = create_response.json()['id']

    updated_data = {
        "title": "Обновленное домашнее задание API"
    }

    # Обновляем проект
    response = project_page.update_project(project_id, updated_data)

    assert response.status_code == 200  # Ожидаем статус 200 OK

    # Получаем проект после обновления и проверяем его название
    get_response = project_page.get_project(project_id)

    assert get_response.status_code == 200  # Ожидаем статус 200 OK
    # Проверяем, что ID соответствует
    assert get_response.json()['id'] == project_id
    # Проверяем обновленное название
    assert get_response.json()['title'] == updated_data['title']


# Получение информации о проекте
def test_get_project_success(project_page):
    # Сначала создаем проект для получения информации
    project_data = {
        "title": "Домашнее задание API",
        "users": {
            "41041360-e041-4300-8eec-fd69f049f1c0": "worker"
        }
    }

    create_response = project_page.create_project(project_data)
    project_id = create_response.json()['id']

    response = project_page.get_project(project_id)

    assert response.status_code == 200  # Ожидаем статус 200 OK
    # Проверяем, что полученный ID соответствует созданному
    assert response.json()['id'] == project_id


# Негативные тесты
# Создание проекта с некорректными данными
def test_create_project_failure_invalid_data(project_page):
    invalid_project_data = {}  # Пустые данные
    response = project_page.create_project(invalid_project_data)
    assert response.status_code == 400  # Ожидаем статус 400 Bad Request


# Изменение несуществующего проекта
def test_update_nonexistent_project(project_page):
    non_existent_id = '1234567890'  # Предполагаемый ID несуществующего проекта
    updated_data = {
        "title": "Обновленное домашнее задание API"
    }

    response = project_page.update_project(non_existent_id, updated_data)
    assert response.status_code == 404  # Ожидаем статус 404 Not Found


# Получение информации о несуществующем проекте
def test_get_nonexistent_project(project_page):
    non_existent_id = '1234567890'  # Предполагаемый ID несуществующего проекта

    response = project_page.get_project(non_existent_id)

    assert response.status_code == 404  # Ожидаем статус 404 Not Found


# Изменение проекта с некорректными данными (например, пустое название)
def test_update_project_failure_invalid_data(project_page):
    # Сначала создаем проект для обновления
    project_data = {
        "title": "Домашнее задание API",
        "users": {
            "41041360-e041-4300-8eec-fd69f049f1c0": "worker"
        }
    }

    create_response = project_page.create_project(project_data)
    project_id = create_response.json()['id']

    invalid_update_data = {
        "title": ""  # Пустое название
    }

    update_response = (project_page.update_project
                       (project_id, invalid_update_data))

    assert update_response.status_code == 400  # Ожидаем статус 400 Bad Request
