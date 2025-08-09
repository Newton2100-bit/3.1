import logging
from logging.handlers import RotatingFileHandler

# Configure logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.INFO)

# Add RotatingFileHandler
handler = RotatingFileHandler(
    'logs/app.log', 
    maxBytes=2 * 1024,   # 2 KB
    backupCount=3
)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Test
for i in range(1000):
    logger.info("This message will rotate logs when maxBytes is reached.")
