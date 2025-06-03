import logging
import os
from datetime import datetime 

# Create log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#  to get current working directory
logs_path = os.path.join(os.getcwd(), "logs")  # Removed LOG_FILE here
os.makedirs(logs_path, exist_ok=True)

#  to provide Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s - %(message)s",
    level=logging.INFO
)

# Main block for testing logging
if __name__ == "__main__":
    logging.info("Logging has started.")
