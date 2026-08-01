
from sqlalchemy import text

import pytest
from src.db.database import engine


@pytest.mark.asyncio
async def test_db():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        assert result.scalar() == 1


