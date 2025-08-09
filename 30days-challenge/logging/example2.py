import logging
import os

# Create logs directory
os.makedirs('logs', exist_ok=True)

class LevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level
        
    def filter(self, record):
        return record.levelno == self.level

# Create logger
logger = logging.getLogger('combined_logger')
logger.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# 1. Create separate file handlers for each level
levels = [
    (logging.DEBUG, 'logs/debug.log'),
    (logging.INFO, 'logs/info.log'),
    (logging.WARNING, 'logs/warning.log'),
    (logging.ERROR, 'logs/error.log'),
    (logging.CRITICAL, 'logs/critical.log')
]

for level, filename in levels:
    handler = logging.FileHandler(filename)
    handler.setLevel(level)
    handler.setFormatter(formatter)
    handler.addFilter(LevelFilter(level))
    logger.addHandler(handler)

# 2. Create a combined file handler for ALL levels
all_handler = logging.FileHandler('logs/all_logs.log')
all_handler.setLevel(logging.DEBUG)
all_handler.setFormatter(formatter)
logger.addHandler(all_handler)

# 3. Optional: Console handler for immediate feedback
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
logger.addHandler(console_handler)

# Test the logger
if __name__ == "__main__":
    logger.debug("Debug: Variable x = 42")
    logger.info("Info: User authentication successful")
    logger.warning("Warning: Memory usage at 85%")
    logger.error("Error: Database connection failed")
    logger.critical("Critical: System overheating detected")
    
    print("\nFiles created:")
    print("Separate files:")
    print("- logs/debug.log (only DEBUG messages)")
    print("- logs/info.log (only INFO messages)")
    print("- logs/warning.log (only WARNING messages)")
    print("- logs/error.log (only ERROR messages)")
    print("- logs/critical.log (only CRITICAL messages)")
    print("\nCombined file:")
    print("- logs/all_logs.log (ALL messages together)")
