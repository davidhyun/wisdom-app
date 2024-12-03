import uvicorn
from apps.app import create_app
from apps.config import Settings

settings = Settings()
app = create_app(settings)


if __name__ == "__main__":
    if settings.ENV == "dev":
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    else:
        uvicorn.run("main:app", host="0.0.0.0", port=8000)