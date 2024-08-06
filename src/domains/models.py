from abc import ABC
from datetime import datetime

from sqlmodel import Field, SQLModel


class BaseModel(SQLModel, ABC):
    """
    Base class for all models
    """

    id: int = Field(default=None, primary_key=True)


class Certification(BaseModel, table=True):
    """
    Certification model
    """

    name: str


class Category(BaseModel, table=True):
    """
    Category model
    """

    cert_id: int = Field(foreign_key="certification.id")
    name: str


class Flashcard(BaseModel, table=True):
    """
    Flashcard model
    """

    cat_id: int = Field(foreign_key="category.id")
    question: str
    answer: str
    number_of_view: int
    last_view_datetime: datetime = Field(default_factory=datetime.utcnow)
