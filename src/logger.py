import logging
import os
from datetime import datetime
import sys

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)  # create logs folder if doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handlers
file_handler = logging.FileHandler(LOG_FILE_PATH)
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

# Create formatters and add them to handlers
formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
