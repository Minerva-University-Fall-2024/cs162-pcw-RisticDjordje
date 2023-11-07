import logging
from logging.handlers import RotatingFileHandler

# Configure the logger
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)

# Create a RotatingFileHandler
handler = RotatingFileHandler('my_log.log', maxBytes=2000, backupCount=5)
handler.setLevel(logging.DEBUG)

# Create a formatter and set the formatter for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Log some messages
for _ in range(20):
    logger.debug('This is a debug message')

# Now if you check the directory where this script is located,
# you will find multiple log files: my_log.log, my_log.log.1, my_log.log.2, etc.
# Each log file (except the current one) will be close to 2000 bytes in size,
# and there will be at most 5 backup log files due to the backupCount parameter.
