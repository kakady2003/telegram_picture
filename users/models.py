from sqlalchemy import String

from src.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from src.db.columns import created_at, updated_at
import uuid

class UserModels(Base):
    __tablename__ = "users"


    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column()

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


