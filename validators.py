import sys
from logger import get_logger

logger = get_logger("validators")


def validate_args(args) -> None:
    if args.quantity <= 0:
        logger.error("Invalid quantity.")
        print("Error: quantity must be greater than 0")
        sys.exit(1)

    if args.order_type == "LIMIT":
        if args.price is None:
            logger.error("Price missing for LIMIT order.")
            print("Error: --price is required for LIMIT orders")
            sys.exit(1)

        if args.price <= 0:
            logger.error("Invalid price.")
            print("Error: price must be greater than 0")
            sys.exit(1)