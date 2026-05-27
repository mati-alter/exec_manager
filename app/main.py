from fastapi import FastAPI

app = FastAPI(title="Exec Manager")


@app.get("/")
async def health() -> dict[str, str]:
    return {"status": "ok"}
