from fastapi.testclient import TestClient
import pytest
from sqlalchemy.orm import Session

from core.config import settings
from tests.utils.cake import create_random_cake, make_random_cake_data
from tests.utils.utils import random_lower_string


def test_create_cake(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"name": "Foo", "comment": "Fighters", "image_url": "https://image_url.com/image/2", "yum_factor": 2}
    response = client.post(
        f"{settings.API_V1_STR}/cakes/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["comment"] == data["comment"]
    assert "id" in content
    assert "owner_id" in content


@pytest.mark.parametrize(
    "prop, bad_value, error_msg",
    [
        ("name", random_lower_string(31), "ensure this value has at most 30 characters"),
        ("comment", random_lower_string(201), "ensure this value has at most 200 characters"),
        ("image_url", random_lower_string(6), "invalid or missing URL scheme"),
        ("yum_factor", 6, "ensure this value is less than or equal to 5"),
        ("yum_factor", 0, "ensure this value is greater than or equal to 1"),

    ]
)
def test_create_cake_with_bad_data(
        client: TestClient, superuser_token_headers: dict, db: Session, prop, bad_value, error_msg
) -> None:
    test_kwargs = {prop: bad_value}
    data = make_random_cake_data(**test_kwargs)
    response = client.post(
        f"{settings.API_V1_STR}/cakes/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 422
    content = response.json()
    msg = content.get("detail")[0].get("msg")
    assert msg == error_msg


@pytest.mark.parametrize(
    "update_fields",
    [
        ("name", "comment"),
        ("image_url", "yum_factor"),
        ("yum_factor", ),
    ]
)
def test_updates_do_allow_optional(
        client: TestClient, superuser_token_headers: dict, db: Session, update_fields
) -> None:
    # Create cake
    cake = create_random_cake(db)

    # Update given fields
    random_data = make_random_cake_data()
    data = dict((field, random_data[field]) for field in update_fields)
    response = client.put(
        f"{settings.API_V1_STR}/cakes/{cake.id}", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    for key, value in data.items():
        assert content[key] == value


def test_read_cake(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    cake = create_random_cake(db)
    response = client.get(
        f"{settings.API_V1_STR}/cakes/{cake.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == cake.name
    assert content["comment"] == cake.comment
    assert content["id"] == cake.id
    assert content["owner_id"] == cake.owner_id
