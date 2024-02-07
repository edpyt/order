from typing import Any
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_product(client: AsyncClient):
    response = await client.post(
        "/product/create/",
        data={"title": "test", "price": "0.1", "weight": 0.5},
    )

    assert response.status_code == 201
    assert response.json() == {"message": "Created product!"}


@pytest.mark.parametrize("create_product_data", [
    {"tsti": "dsaj", "dsajdjsa": .1, "erd": "E"},
    {"dsad": .1},
    [1, 2, 3, 4]
])
@pytest.mark.asyncio
async def test_wrong_create_product(client: AsyncClient, create_product_data: Any):
    response = await client.post("/product/create/", data=create_product_data)

    assert response.status_code == 400
