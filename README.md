# Binance Futures Testnet Trading Bot

Python CLI app to place MARKET and LIMIT orders on Binance Futures Testnet.

## Features

- BUY / SELL support
- MARKET / LIMIT orders
- Input validation
- Error handling
- Logging to file

## Setup

pip install -r requirements.txt

Create `.env` using `.env.example`

## Run Examples

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 95000