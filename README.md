# HH Agent

Python-приложение для поиска вакансий на HeadHunter, уведомлений в Telegram и будущей автоматизации откликов.

## Локальный запуск API без Docker

```powershell
uv run uvicorn hh_agent.main:app --reload
```

## Настройки

Создай локальный `.env` на основе `.env.example`:

```powershell
Copy-Item .env.example .env
```

Файл `.env` хранит локальные секреты и не должен попадать в git.

## Локальный запуск через Docker

Запуск API и PostgreSQL:

```powershell
docker compose up -d
```

Логи API:

```powershell
docker compose logs api -f
```

Проверка подключения из API:

```text
http://127.0.0.1:8000/health/db
```

## Миграции базы данных

Применить миграции:

```powershell
docker compose run --rm api uv run alembic upgrade head
```

Проверить текущую версию схемы:

```powershell
docker compose run --rm api uv run alembic current
```
