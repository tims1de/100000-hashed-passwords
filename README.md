# Сервис на основе 100000 хэшированнных паролей

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat-square&logo=Alembic)](https://alembic.sqlalchemy.org/en/latest/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat-square&logo=SQLAlchemy)](https://www.sqlalchemy.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![Uvicorn](https://img.shields.io/badge/-Uvicorn-464646?style=flat-square&logo=uvicorn)](https://www.uvicorn.org/)
[![Gunicorn](https://img.shields.io/badge/-Gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![JavaScript](https://img.shields.io/badge/-JavaScript-464646?style=flat-square&logo=javascript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![React](https://img.shields.io/badge/-React-464646?style=flat-square&logo=react)](https://react.dev/)
[![Vite](https://img.shields.io/badge/-Vite-464646?style=flat-square&logo=vite)](https://vite.dev/)
[![npm](https://img.shields.io/badge/-Npm-464646?style=flat-square&logo=Npm)](https://www.npmjs.com/)
[![Node.js](https://img.shields.io/badge/-Node.js-464646?style=flat-square&logo=Node.js)](https://nodejs.org/en)
[![Ruff](https://img.shields.io/badge/-Ruff-464646?style=flat-square&logo=Ruff)](https://docs.astral.sh/ruff/)

# Описание 

Сервис позволяет на основе 100000 самых распространенных паролей мира по введенному хешу определить базовый пароль. Используется SHA-256. Бэкенд на Python (FastAPI) использует асинхронную обработку и мгновенно проверяет хеши через предзагруженный набор данных. Фронтенд на React (Vite) предлагает форму ввода и отображение результатов. Развертывание — локально (Python/Node.js) или в Docker-контейнерах. Для форматирования кода использовался линтер и форматер Ruff.

#### Локально документация доступна по адресу: <http://localhost:8000/docs/>, а также <http://localhost:5173/>.

#### Локальный запуск проекта

- Предварительно необходимо установить Docker для вашей системы.

- Склонировать репозиторий:
  
```
   git clone <название репозитория>
```

Cоздать и активировать виртуальное окружение:

Команды для установки виртуального окружения на Mac или Linux:

```
   python3 -m venv env
   source env\bin\activate
```

Команды для Windows:

```
   python -m venv venv
   source venv\Scripts\activate
```

- Создать файл .env и .env-non-dev по образцу:

```bash
   cp .env-non-dev .env
```

- Файл .env:

```bash
  DB_HOST=*****
  DB_PORT=*****
  DB_USER=*****
  DB_PASS=*****
  DB_NAME=*****
```

- Файл .env-non-dev:

```bash
  DB_HOST=*****
  DB_PORT=*****
  DB_USER=*****
  DB_PASS=*****
  DB_NAME=*****

  POSTGRES_DB=*****
  POSTGRES_USER=*****
  POSTGRES_PASSWORD=*****
```

- Установить зависимости из файла requirements.txt:

```bash
   cd ..
   pip install -r requirements.txt
```

- Для создания миграций выполнить команду:

```bash
   alembic init migrations
```

- Инициализировать БД:

``` bash
    alembic revision --autogenerate -m "comment"
```

- Применить миграцию:

``` bash
    alembic upgrade head
```

- Запустить проект:

``` bash
    uvicorn main:app --reload
```

#### Пример обычного пароля и его хешированной версии 

```
Обычный - password
Хешированный - 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
```

#### Запуск docker-compose

```
  docker compose up --build
```

#### Автор

Куприянов Тимофей - [https://github.com/tims1de](https://github.com/tims1de)
