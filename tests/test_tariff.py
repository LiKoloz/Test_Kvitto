async def test_get_all_tariffs(client):
    base = [
    {
        "title": "basic",
        "price": 990000,
        "id": 1
    },
    {
        "title": "standard",
        "price": 1990000,
        "id": 2
    },
    {
        "title": "premium",
        "price": 2990000,
        "id": 3
    }
]
    r = await client.get("/tariffs/")
    assert r.status_code == 200

    data = r.json()
    assert len(data) == 3

    for item, expected in zip(data, base):
        assert item["id"] == expected["id"]
        assert item["title"] == expected["title"]
        assert item["price"] == expected["price"]
        assert "created_at" in item          
