# Library Project

Учебное консольное приложение для управления библиотекой.

Проект создан для практики разработки на Python, работы с PostgreSQL, объектно-ориентированного программирования, слоистой архитектуры, Dependency Injection, Git и автоматизированного тестирования.

## Возможности

### Книги

* просмотр списка книг;
* поиск книги по ID;
* добавление книги;
* изменение книги;
* удаление книги;
* сортировка и фильтрация.

### Авторы

* просмотр списка авторов;
* поиск автора по ID;
* добавление автора;
* изменение автора;
* удаление автора.

### Издательства

* просмотр списка издательств;
* поиск издательства по ID;
* добавление издательства;
* изменение издательства;
* удаление издательства.

## Технологии

* Python 3.13+
* PostgreSQL
* psycopg 3
* pytest
* pytest-cov
* python-dotenv
* Git
* GitHub

## Архитектура

Проект использует слоистую архитектуру:

```text
UI
 ↓
Services
 ↓
Repository Interfaces
 ↓
Repositories
 ↓
PostgreSQL
```

### Основные слои

**Models**

Dataclass-модели предметной области:

* `Book`
* `Author`
* `Publisher`

**Repositories**

Отвечают за работу с базой данных.

**Repository Interfaces**

Определяют интерфейсы репозиториев и позволяют сервисам не зависеть от конкретной реализации базы данных.

**Services**

Содержат бизнес-логику приложения.

**Validators**

Отвечают за проверку корректности данных перед выполнением операций.

**UI**

Содержит консольное взаимодействие с пользователем.

## Структура проекта

```text
library_project/
│
├── models/
│   ├── author.py
│   ├── book.py
│   └── publisher.py
│
├── repositories/
│   ├── interfaces/
│   │   ├── author_repository.py
│   │   ├── book_repository.py
│   │   └── publisher_repository.py
│   │
│   ├── author_repository.py
│   ├── book_repository.py
│   └── publisher_repository.py
│
├── services/
│   ├── author_service.py
│   ├── book_service.py
│   └── publisher_service.py
│
├── validators/
│   ├── author_validator.py
│   └── book_validator.py
│
├── ui/
│   ├── main_menu.py
│   ├── book_menu.py
│   ├── author_menu.py
│   └── publisher_menu.py
│
├── tests/
│   ├── conftest.py
│   ├── test_author.py
│   ├── test_book.py
│   ├── test_publisher.py
│   ├── test_author_repository.py
│   ├── test_book_repository.py
│   ├── test_publisher_repository.py
│   ├── test_author_service.py
│   ├── test_book_service.py
│   ├── test_publisher_service.py
│   ├── test_author_validator.py
│   └── test_book_validator.py
│
├── config.py
├── database.py
├── exception_library.py
├── schema.sql
├── requirements.txt
├── .env.example
└── main.py
```

## Установка

Клонировать репозиторий:

```bash
git clone <repository-url>
cd library_project
```

Создать виртуальное окружение:

```bash
python3 -m venv venv
```

Активировать его:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Настройка PostgreSQL

Для работы проекта необходим установленный и запущенный PostgreSQL.

Создайте базу данных:

```sql
CREATE DATABASE library;
```

После этого выполните SQL-код из файла:

```text
schema.sql
```

Файл содержит структуру базы данных, включая таблицы, первичные и внешние ключи и ограничения.

## Настройка переменных окружения

Создайте в корне проекта файл `.env`.

Пример конфигурации находится в:

```text
.env.example
```

Пример:

```env
DB_NAME=library
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Файл `.env` не должен добавляться в Git.

## Запуск приложения

После настройки базы данных и `.env` запустите:

```bash
python main.py
```

## Тестирование

Запустить все тесты:

```bash
pytest
```

Запустить тесты с подробным выводом:

```bash
pytest -v
```

## Coverage

Для получения отчёта о покрытии:

```bash
pytest --cov=. --cov-report=term-missing
```

Текущий проект имеет около **96% покрытия кода**.

Основная бизнес-логика, репозитории, сервисы и валидаторы покрыты тестами.

## База данных

Основные таблицы проекта:

* `authors`
* `publishers`
* `books_join`

Книги связаны с авторами и издательствами через внешние ключи.

## Цель проекта

Основная цель проекта — закрепить на практике:

* Python;
* ООП;
* PostgreSQL;
* SQL;
* Repository Pattern;
* Dependency Injection;
* интерфейсы;
* валидацию данных;
* работу с Git и GitHub;
* unit-тестирование;
* integration-тестирование;
* pytest и code coverage.
