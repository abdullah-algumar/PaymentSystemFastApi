from fastapi import FastAPI, HTTPException
from app.database import engine, SessionLocal
from app.models import Transaction, TransactionCreate, TransactionUpdate
from datetime import datetime
from fastapi.openapi.utils import get_openapi

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Payment Transaction API",
        version="0.1.0",
        description="This is a simple API to manage payment transactions.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.post("/transactions/")
def create_transaction(transaction: TransactionCreate):
    db = SessionLocal()
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.get("/transactions/{id}")
def get_transaction(id: int):
    db = SessionLocal()
    transaction = db.query(Transaction).filter(Transaction.id == id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@app.get("/transactions/")
def get_transactions():
    db = SessionLocal()
    transactions = db.query(Transaction).all()
    return transactions

@app.patch("/transactions/{id}")
def update_transaction(id: int, transaction: TransactionUpdate):
    db = SessionLocal()
    db_transaction = db.query(Transaction).filter(Transaction.id == id).first()
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db_transaction.status = transaction.status
    db_transaction.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
