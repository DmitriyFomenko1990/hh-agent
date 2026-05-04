from fastapi import FastAPI

app = FastAPI(title="HH Agent")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
