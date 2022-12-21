from pydantic import BaseModel, Field


class PostRequest(BaseModel):
    from_: str = Field(alias="from")
    to_: str = Field(alias="to")


class ExchangeRatesResults(BaseModel):
    # from_currency: str = Field(alias="1. From_Currency Code")
    # to_currency: str = Field(alias="3. To_Currency Code")
    exchange_rate: float = Field(alias="5. Exchange Rate")


class AlphavantageResponse(BaseModel):
    results: ExchangeRatesResults = Field(alias="Realtime Currency Exchange Rate")
