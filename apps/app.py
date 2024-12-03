from fastapi import FastAPI
from apps.config import Settings
from apps.quote import view

def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.DESCRIPTION,
        docs_url="/docs"
    )
    
    app.include_router(view.router)
    
    return app