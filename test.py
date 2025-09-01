# Import logging and beetle packages
import logging
from beetle_logging import beetle

# Init the beetle class
bt = beetle(__name__, fileLogging=False)

# Set logging level
bt.setStreamLevel(logging.DEBUG)

# Create messages!
bt.logger.debug("This is a debug message")
bt.logger.info("This is an info message")
bt.logger.error("This is an error")
bt.logger.critical("This is a critical message")


# Or create messages using the logger class!
logger = logging.getLogger(__name__)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.error("This is an error")
logger.critical("This is a critical message")