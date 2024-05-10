from typing import Optional, Dict, List
from pgvector.sqlalchemy import Vector
from sqlmodel import Field, SQLModel, JSON, Column, create_engine

from settings import Settings

engine = create_engine(Settings().db_url)


class Document(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    meta: Optional[Dict] = Field(default={}, sa_column=Column(JSON))
    embedding: List[float] = Field(sa_column=Column(Vector(1024)))
    document: Optional[str]

    class Config:
        arbitrary_types_allowed = True


SQLModel.metadata.create_all(engine)
