from fastapi import FastAPI

from resources.router import api_router


def get_app() -> FastAPI:
    fast_app = FastAPI(title="Ingaia Api", version="0.0.1", debug=True)
    fast_app.include_router(api_router, prefix="/api")

    return fast_app


app = get_app()
