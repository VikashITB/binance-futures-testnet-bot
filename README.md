# Binance Futures Testnet Trading Bot

A Python CLI application for placing MARKET and LIMIT orders on the Binance USDT-M Futures Testnet. Showcases practical API integration, modular Python design, structured logging, and reliable error handling.
> ✅ Tested successfully with MARKET and LIMIT orders on Binance Futures Testnet.

---

## Features

- Place MARKET and LIMIT orders from the command line
- Supports BUY and SELL on any valid USDT-M futures symbol
- Input validation before any API call is made
- Persistent logging to file with timestamps and log levels
- Graceful error handling for API failures and bad input
- Modular codebase — each concern lives in its own file

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| `binance-futures-connector` | Official Binance Futures SDK |
| `python-dotenv` | Load API credentials from `.env` |
| `argparse` | CLI argument parsing |
| `logging` | File + console log output |

---

## Project Structure

```
binance-futures-testnet-bot/
├── cli.py              # Entry point — argument parsing and orchestration
├── validators.py       # Pre-API input validation
├── client.py           # Binance Futures Testnet client setup
├── order.py            # MARKET and LIMIT order logic
├── logger.py           # Logging configuration (file + console)
├── config.py           # Environment variables and constants
├── logs/
│   ├── trading_bot.log       # Generated at runtime
│   ├── sample_market.log     # Sample MARKET order output
│   └── sample_limit.log      # Sample LIMIT order output
├── .env.example        # Credential template
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Get Testnet API Credentials

1. Go to [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
2. Sign in with your GitHub account
3. Click **API Key** to generate a key/secret pair

### 2. Install Dependencies

```bash
git clone https://github.com/VikashITB/binance-futures-testnet-bot.git
cd binance-futures-testnet-bot

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 3. Configure Credentials

```bash
cp .env.example .env
```

Edit `.env` and add your testnet keys:

```
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here
```

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `BINANCE_API_KEY` | Yes | Testnet API key from binancefuture.com |
| `BINANCE_API_SECRET` | Yes | Testnet API secret |

These are loaded automatically from `.env` at runtime via `python-dotenv`.

---

## How to Run

All commands are run from the project root directory.

```
python cli.py --symbol <SYMBOL> --side <BUY|SELL> --type <MARKET|LIMIT> --quantity <QTY> [--price <PRICE>]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `--symbol` | Yes | Trading pair, e.g. `BTCUSDT` |
| `--side` | Yes | `BUY` or `SELL` |
| `--type` | Yes | `MARKET` or `LIMIT` |
| `--quantity` | Yes | Order size in base asset units |
| `--price` | LIMIT only | Limit price (required when `--type LIMIT`) |

---

## Example Commands

**MARKET BUY**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**MARKET SELL**
```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.01
```

**LIMIT BUY**
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 60000
```

**LIMIT SELL**
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.1 --price 3200
```

---

## Sample Output

```
INFO: Placing MARKET BUY order | Symbol: BTCUSDT | Qty: 0.01

==================================================
  ORDER PLACED SUCCESSFULLY
==================================================
  Order ID     : 3822945612
  Symbol       : BTCUSDT
  Side         : BUY
  Type         : MARKET
  Status       : NEW
  Quantity     : 0.01
  Executed Qty : 0.01
  Avg Price    : 62345.10
==================================================

Full response logged to logs/trading_bot.log
```

For a LIMIT order, `Status` will show `NEW` (order is open and waiting to be filled) and `Avg Price` will be `0` until execution.

---

## Logging

Runtime logs are written to `logs/trading_bot.log` and also printed to the console at INFO level.

```
2024-05-10 14:31:58 | INFO     | cli   | CLI invoked | symbol=BTCUSDT side=BUY type=MARKET quantity=0.01
2024-05-10 14:31:59 | INFO     | order | MARKET order placed successfully | Order ID: 3822945612
2024-05-10 14:31:59 | DEBUG    | order | Full response: {'orderId': 3822945612, 'status': 'NEW', ...}
```

- `DEBUG` — Full API response payloads
- `INFO` — Order events and CLI activity
- `ERROR` — API errors with status codes and messages

Sample log files are included in `logs/` for reference.

---

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Missing API credentials | Exits before any network call with a clear message |
| `--price` omitted for LIMIT order | Caught by `validators.py`, exits cleanly |
| Negative or zero quantity / price | Caught by `validators.py`, exits cleanly |
| Binance `ClientError` (4xx) | Logs HTTP status, Binance error code, and message |
| Binance `ServerError` (5xx) | Logged and exits gracefully |
| Unexpected exceptions | Full traceback written to log; user sees a clean message |

---

## Notes & Assumptions

- This project targets the **Binance Futures Testnet only**. The base URL is hardcoded to `https://testnet.binancefuture.com` — no real funds are ever used.
- LIMIT orders are placed with `timeInForce=GTC` (Good Till Cancelled), which is the standard default for futures limit orders.
- Symbols are automatically uppercased (`btcusdt` → `BTCUSDT`) to prevent avoidable input errors.
- The `logs/` directory is created automatically at runtime if it does not exist.
- MARKET and LIMIT orders were both tested successfully on the Binance Futures Testnet.

---

## About This Project

This was built as part of a Python Developer hiring assignment. The goal was to demonstrate practical API integration, clean modular code structure, and production-minded practices — not just a working script, but something that could realistically be extended, maintained, or reviewed by another developer.
