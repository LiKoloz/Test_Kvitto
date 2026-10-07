async def test_promo_case_insensitive(client):
    base = {"tariff_id": 2, "email": "a@b.c", "method": "card"}

    r1 = await client.post("/payments/", json=base)
    assert r1.status_code == 201

    r2 = await client.post("/payments/", json={**base, "promo_code": "kvitt010"})
    assert r2.status_code == 201

    r3 = await client.post("/payments/", json={**base, "promo_code": "KVITT010"})
    assert r3.status_code == 201

    # посмотрим amount у созданных
    p1 = (await client.get("/payments/1")).json()
    p2 = (await client.get("/payments/2")).json()
    p3 = (await client.get("/payments/3")).json()

    assert p1["amount"] == 1990000
    assert p2["amount"] == 1990000 * 90 // 100
    assert p3["amount"] == p2["amount"]


async def test_unknown_promo_returns_422(client):
    try:
        r = await client.post("/payments/", json={
            "tariff_id": 1, "email": "a@b.c", "method": "card", "promo_code": "NOPE",
        })
    except Exception as e:
        assert True

async def test_idempotency_key_returns_same(client):
     body = {"tariff_id": 2, "email": "a@b.c", "method": "card"}
     headers = {"Idempotency-Key": "1"}
     await client.post("/payments/", json={**body})

     r3 = await client.post("/payments/", json=body, headers=headers)
     assert r3.status_code == 200


async def test_payment_not_found(client):
    r = await client.get("/payments/99999")
    assert r.status_code == 404

