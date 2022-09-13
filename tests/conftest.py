import pytest
from requests_mock import Mocker
from typing import Iterator
from alpaca.broker.client import BrokerClient
import requests_mock

from alpaca.data.historical import StockHistoricalDataClient, NewsHistoricalDataClient, CryptoHistoricalDataClient
from alpaca.trading.client import TradingClient


@pytest.fixture
def reqmock() -> Iterator[Mocker]:
    with requests_mock.Mocker() as m:
        yield m


@pytest.fixture
def client():
    client = BrokerClient(
        "key-id",
        "secret-key",
        sandbox=True,  # Expressly call out sandbox as true for correct urls in reqmock
    )
    return client


@pytest.fixture
def raw_client():
    raw_client = BrokerClient("key-id", "secret-key", raw_data=True)
    return raw_client


@pytest.fixture
def trading_client():
    client = TradingClient("key-id", "secret-key")
    return client


@pytest.fixture
def stock_client():
    client = StockHistoricalDataClient("key-id", "secret-key")
    return client


@pytest.fixture
def raw_stock_client():
    raw_client = StockHistoricalDataClient("key-id", "secret-key", raw_data=True)
    return raw_client


@pytest.fixture
def crypto_client():
    client = CryptoHistoricalDataClient("key-id", "secret-key")
    return client


@pytest.fixture
def raw_crypto_client():
    raw_client = CryptoHistoricalDataClient("key-id", "secret-key", raw_data=True)
    return raw_client

@pytest.fixture
def news_client():
    client = NewsHistoricalDataClient("key-id", "secret-key")
    return client