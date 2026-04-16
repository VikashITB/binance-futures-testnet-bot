import argparse
import sys

from config import VALID_SIDES, VALID_ORDER_TYPES
from client import get_client
from order import place_market_order, place_limit_order
from validators import validate_args
from logger import get_logger

logger = get_logger("cli")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Place MARKET or LIMIT orders on Binance Futures Testnet."
    )

    parser.add_argument("--symbol", required=True, type=str)
    parser.add_argument(
        "--side",
        required=True,
        type=str.upper,
        choices=VALID_SIDES
    )
    parser.add_argument(
        "--type",
        dest="order_type",
        required=True,
        type=str.upper,
        choices=VALID_ORDER_TYPES
    )
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    return parser.parse_args()


def print_result(response: dict) -> None:
    avg_price = response.get("avgPrice", "0")
    executed_qty = response.get("executedQty", "0")

    print("\n" + "=" * 50)
    print("ORDER SUBMITTED")
    print("=" * 50)
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Symbol       : {response.get('symbol')}")
    print(f"Side         : {response.get('side')}")
    print(f"Type         : {response.get('type')}")
    print(f"Status       : {response.get('status')}")
    print(f"Quantity     : {response.get('origQty')}")
    print(f"Executed Qty : {executed_qty}")

    if response.get("price"):
        print(f"Price        : {response.get('price')}")

    if float(avg_price) > 0:
        print(f"Avg Price    : {avg_price}")

    print("=" * 50)
    print("SUCCESS\n")


def main():
    args = parse_args()
    validate_args(args)

    logger.info(
        f"Request | {args.symbol} {args.side} "
        f"{args.order_type} qty={args.quantity}"
    )

    try:
        client = get_client()

        if args.order_type == "MARKET":
            response = place_market_order(
                client,
                args.symbol,
                args.side,
                args.quantity
            )
        else:
            response = place_limit_order(
                client,
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print_result(response)

    except Exception as e:
        logger.exception(str(e))
        print(f"FAILURE: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()