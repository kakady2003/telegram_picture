from sqlalchemy import text
import pytest


@pytest.mark.asyncio
async def test_db(db_session):
    result = await db_session.execute(text("SELECT 1"))

    assert result.scalar() == 1