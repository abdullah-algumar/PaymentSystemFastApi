from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_transaction():
    transaction_data = {
        "amount": 100,
        "currency": "USD"
    }
    response = client.post("/transactions/", json=transaction_data)
    assert response.status_code == 200
    transaction = response.json()
    assert transaction["amount"] == transaction_data["amount"]
    assert transaction["currency"] == transaction_data["currency"]
    assert transaction["status"] == "pending"

def test_get_transaction():
    response = client.post("/transactions/", json={"amount": 200, "currency": "EUR"})
    transaction_id = response.json()["id"]

    response = client.get(f"/transactions/{transaction_id}")
    assert response.status_code == 200
    transaction = response.json()
    assert transaction["id"] == transaction_id

def test_get_transactions():
    response = client.get("/transactions/")
    assert response.status_code == 200
    transactions = response.json()
    assert len(transactions) > 0

def test_update_transaction():
    response = client.post("/transactions/", json={"amount": 300, "currency": "GBP"})
    transaction_id = response.json()["id"]

    update_data = {
        "status": "completed"
    }
    response = client.patch(f"/transactions/{transaction_id}", json=update_data)
    assert response.status_code == 200
    updated_transaction = response.json()
    assert updated_transaction["status"] == "completed"
