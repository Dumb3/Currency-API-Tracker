from model.db_model import Currency
from database.connection import SessionLocal

def save_currency(currency: str, value: float):
    db = SessionLocal()
    new_currency = Currency(currency=currency, value=value)
    db.add(new_currency)
    db.commit()
    db.refresh(new_currency)
    db.close()
    return new_currency

def get_last_currencies(limit: int = 10):
    db = SessionLocal()
    data = db.query(Currency)\
        .order_by(Currency.timestamp.desc())\
        .limit(limit)\
        .all()
    db.close()
    return data
