from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./library.db"
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    from app.models.user import User
    from app.models.book import Book
    from app.models.borrow_record import BorrowRecord
    SQLModel.metadata.create_all(engine)