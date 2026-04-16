from binance.um_futures import UMFutures
from binance.error import ClientError, ServerError
from logger import get_logger

logger = get_logger("order")


def place_market_order(
    client: UMFutures,
    symbol: str,
    side: str,
    quantity: float
) -> dict:
    logger.info(f"Placing MARKET {side} order | {symbol} | Qty={quantity}")

    try:
        response = client.new_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="MARKET",
            quantity=quantity,
        )

        logger.info(
            f"MARKET order placed successfully | ID={response.get('orderId')}"
        )
        logger.debug(response)

        return response

    except ClientError as e:
        logger.error(f"Client error: {e}")
        raise

    except ServerError as e:
        logger.error(f"Server error: {e}")
        raise


def place_limit_order(
    client: UMFutures,
    symbol: str,
    side: str,
    quantity: float,
    price: float
) -> dict:
    logger.info(
        f"Placing LIMIT {side} order | {symbol} | Qty={quantity} | Price={price}"
    )

    try:
        response = client.new_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )

        logger.info(
            f"LIMIT order placed successfully | ID={response.get('orderId')}"
        )
        logger.debug(response)

        return response

    except ClientError as e:
        logger.error(f"Client error: {e}")
        raise

    except ServerError as e:
        logger.error(f"Server error: {e}")
        raise