from fastapi import FastAPI
from routers import composers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  #allow cookies
    allow_methods=["*"],
    allow_headers=["*"],     #allow header (token)
)


app.include_router(composers.router)