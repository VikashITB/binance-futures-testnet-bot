from binance.um_futures import UMFutures
from config import API_KEY, API_SECRET, TESTNET_BASE_URL
from logger import get_logger

logger = get_logger("client")


def get_client() -> UMFutures:
    if not API_KEY or not API_SECRET:
        logger.error("API credentials missing.")
        raise ValueError(
            "Set BINANCE_API_KEY and BINANCE_API_SECRET in .env file."
        )

    client = UMFutures(
        key=API_KEY,
        secret=API_SECRET,
        base_url=TESTNET_BASE_URL,
    )

    logger.info("Connected to Binance Futures Testnet.")
    return client