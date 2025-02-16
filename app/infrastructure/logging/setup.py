import logging.config
from app.infrastructure.config.logging_config import LOGGING_CONFIG

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)