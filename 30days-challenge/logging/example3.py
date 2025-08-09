import logging

# You CANNOT do this with basicConfig - it only supports one file
# logging.basicConfig(filename=['file1.log', 'file2.log'])  # This won't work!

# Instead, you need to create multiple handlers manually
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Handler 1: All logs to main file
main_handler = logging.FileHandler('main.log')
main_handler.setLevel(logging.DEBUG)
main_handler.setFormatter(formatter)
logger.addHandler(main_handler)

# Handler 2: Only errors to error file
error_handler = logging.FileHandler('errors.log')
error_handler.setLevel(logging.ERROR)  # Only ERROR and CRITICAL
error_handler.setFormatter(formatter)
logger.addHandler(error_handler)

# Handler 3: Console output
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Test it
if __name__ == "__main__":
    logger.debug("Debug message")     # Goes to: main.log only
    logger.info("Info message")       # Goes to: main.log + console
    logger.warning("Warning message") # Goes to: main.log + console
    logger.error("Error message")     # Goes to: main.log + console + errors.log
    logger.critical("Critical message") # Goes to: main.log + console + errors.log
    
    print("\nFiles created:")
    print("- main.log (all messages)")
    print("- errors.log (only ERROR and CRITICAL)")
    print("- Console output (INFO and above)")
