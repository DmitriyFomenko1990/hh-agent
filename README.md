# HH Agent

Python-приложение для поиска вакансий на HeadHunter, уведомлений в Telegram и будущей автоматизации откликов.

## Локальный запуск API

```powershell
uv run uvicorn --app-dir src hh_agent.main:app --reload
```

## Настройки

Создай локальный `.env` на основе `.env.example`:

```powershell
Copy-Item .env.example .env
```

Файл `.env` хранит локальные секреты и не должен попадать в git.
