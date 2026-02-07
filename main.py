from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from model.db_model import Base
from database.connection import engine
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from service.exchange_service import fetch_currency
from repository.db_repository import (
    save_currency,
    get_last_currencies
)
from schema.api_schema import CurrencyResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Currency Tracker API")

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request})


@app.get("/cotacao/{currency}", response_model=CurrencyResponse)
def get_currency(currency: str):
    value = fetch_currency(currency)

    if value is None:
        raise HTTPException(status_code=400, detail="Currency not supported")

    saved = save_currency(currency, value)
    return saved

@app.get("/historico", response_model=list[CurrencyResponse])
def get_history():
    return get_last_currencies()


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id}
    )