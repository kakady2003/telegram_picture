from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_session
from users.models import UserModels
from users.schemas import UserCreateSchemas, UserReadSchemas
from users.service import hash_password

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserReadSchemas)
async def create_user(
        user: UserCreateSchemas,
        session: AsyncSession = Depends(get_session),
) -> UserReadSchemas:
    print("RAW PASSWORD:", user.password, len(user.password))

    hashed_password = hash_password(user.password)

    db_user = UserModels(
        username=user.username,
        email=user.email,
        password=hashed_password,
    )

    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)

    return UserReadSchemas.model_validate(db_user)
