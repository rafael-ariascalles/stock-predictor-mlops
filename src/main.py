from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from src.model import predict, convert

app = FastAPI()

# pydantic models
class StockIn(BaseModel):
    ticker: str
    days: int

class StockOut(StockIn):
    forecast: dict

@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    """ Endpoint to predict stock price
    Args:
        payload (StockIn): Payload containing ticker and days
    Returns:
        StockOut: Payload containing forecast
    """

    ticker = payload.ticker
    days = payload.days

    prediction_list = predict(ticker, days)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {
        "ticker": ticker, 
        "days": days,
        "forecast": convert(prediction_list)
    }
    
    return response_object