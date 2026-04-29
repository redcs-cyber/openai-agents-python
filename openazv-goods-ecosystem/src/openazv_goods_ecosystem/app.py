from fastapi import FastAPI

from .settings import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, version=settings.version)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "environment": settings.environment, "version": settings.version}

    @app.get("/ready")
    def ready() -> dict[str, str]:
        return {"status": "ready"}

    return app


app = create_app()
