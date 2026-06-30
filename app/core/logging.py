import sys

from loguru import logger

# Remove the default logger
logger.remove()

# Console logger
logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
           "{message}"
)

# File logger
logger.add(
    "logs/application.log",
    rotation="10 MB",
    retention="7 days",
    compression="zip",
    level="DEBUG",
    enqueue=True
)