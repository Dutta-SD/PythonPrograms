from fastapi import FastAPI

from apis.general_pages.route_homepage import general_pages_router
from core.config import settings


def include_router(app: FastAPI):
    app.include_router(general_pages_router)


def start_application():
    app: FastAPI = FastAPI(
        title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION
    )
    include_router(app)
    return app


app = start_application()
