from fastapi import FastAPI
from routers import composers

app = FastAPI()

app.include_router(composers.router)