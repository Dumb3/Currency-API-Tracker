from pydantic import BaseModel
from datetime import datetime

class CurrencyResponse(BaseModel):
    currency: str
    value: float
    timestamp: datetime

    class Config:
        from_attributes = True
