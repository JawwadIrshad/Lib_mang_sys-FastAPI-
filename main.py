from fastapi import FastAPI
from app.routers import auth, books, borrow, users
from app.database import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(books.router, prefix="/api/books", tags=["Books"])
app.include_router(borrow.router, prefix="/api/borrow", tags=["Borrow"])