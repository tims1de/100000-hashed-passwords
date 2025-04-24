from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Passwords(Base):
    __tablename__ = "passwords"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

