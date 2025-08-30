
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class BorrowRecord(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    book_id: int = Field(foreign_key="book.id")
    borrow_date: datetime = Field(default_factory=datetime.utcnow)
    return_date: Optional[datetime] = None
    status: str  # "borrowed" or "returned"
    due_date: datetime
