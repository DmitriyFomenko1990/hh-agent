from fastapi import FastAPI

from hh_agent.core.settings import get_settings

settings = get_settings()

app = FastAPI(title=settings.app_name, debug=settings.debug)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
