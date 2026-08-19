import pytest
import uuid

@pytest.mark.asyncio
async def test_create_users(client):
    username = f"test_{uuid.uuid4().hex[:8]}"
    email = f"{username}@test.com"

    response = await client.post(
        "/users/",
        json={
            "username": username,
            "email": email,
            "password": "afdasdfasd",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == username
    assert data["email"] == email