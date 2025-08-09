import logging

# create and configure logger
logging.basicConfig(filename = './logs/lumberjack.log')
logger = logging.getLogger() # working with th eroot loger (nameless)

# Test the logger
logger.info("Our first message.")
print('Our loger level is ',logger.level)
