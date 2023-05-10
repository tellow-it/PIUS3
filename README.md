# PIUS3
To do API

## Структура проекта
```
├───alembic - миграции
│   │   env.py
│   │   README
│   │   script.py.mako
│   │
│   ├───versions
│   │   │   3bcb098061a3_initial.py
│
├───apis - API
│   │   base.py
│   │
│   ├───version_1
│   │   │   router_category.py
│   │   │   router_important.py
│   │   │   router_task.py
│
├───core - Настройка конфига
│   │   config.py
│
├───db - ORM
│   │   base.py
│   │   base_class.py
│   │   session.py
│   │
│   ├───models - Инициализация моделей
│   │   │   categories.py
│   │   │   important.py
│   │   │   tasks.py
│   │   │   __init__.py
│   │
│   ├───repository - CRUD операции для моделей
│   │   │   categories.py
│   │   │   important.py
│   │   │   tasks.py
│
├───schemas - Схемы Response, Request
│   │   base_schema.py
│   │   category.py
│   │   important.py
│   │   task.py
│
├───tests - тесты
│   │   test_app.py
│   │   __init__.py
```
## Запуск проекта
```
python -m venv .venv
pip install -r requirments.txt
uvicorn main:app --reload
```
## Запуск тестов
```
pytest -v
```
