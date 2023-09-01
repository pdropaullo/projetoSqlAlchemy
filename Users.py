from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from Base import Base

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))