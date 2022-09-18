from loguru import logger
import requests
import os

class GLogger():
    def __init__(self) -> None:
        pass
    
    def info(self, msg):
        logger.info(msg)
    
    def debug(self, msg):
        logger.debug(msg)
    
    def warning(self, msg):
        logger.warning(msg)
    
    def error(self, msg):
        logger.error(msg)

    def critical(self, msg):
        logger.critical(msg)