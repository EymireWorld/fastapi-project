from fastapi import FastAPI

from app.api import router as api_router


app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)
app.include_router(api_router)


@app.get('/')
def index():
    return {'message': 'hello world'}
