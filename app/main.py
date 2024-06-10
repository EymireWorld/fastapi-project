from fastapi import FastAPI
from app.api.tasks.router import router as tasks_router
from app.api.auth.router import router as auth_router


app = FastAPI()
app.include_router(tasks_router)
app.include_router(auth_router)


@app.get('/')
def index():
    return {'message': 'hello world'}
