import logging
import os

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Custom filter to allow only specific log levels
class LevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level
        
    def filter(self, record):
        return record.levelno == self.level

# Create logger
logger = logging.getLogger('multi_file_logger')
logger.setLevel(logging.DEBUG)  # Set to lowest level to capture everything

# Create formatters
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create handlers for each log level
levels = [
    (logging.DEBUG, 'logs/debug.log'),
    (logging.INFO, 'logs/info.log'),
    (logging.WARNING, 'logs/warning.log'),
    (logging.ERROR, 'logs/error.log'),
    (logging.CRITICAL, 'logs/critical.log')
]

for level, filename in levels:
    # Create file handler
    handler = logging.FileHandler(filename)
    handler.setLevel(level)
    handler.setFormatter(formatter)
    
    # Add filter to only capture this specific level
    handler.addFilter(LevelFilter(level))
    
    # Add handler to logger
    logger.addHandler(handler)

# Test the logger
if __name__ == "__main__":
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
    print("Check the 'logs' directory for separate files!")
    print("- debug.log")
    print("- info.log") 
    print("- warning.log")
    print("- error.log")
    print("- critical.log")
