import sys
from src.logger import logging  # Make sure src/logger/__init__.py exists

def error_message_detail(error, error_detail: sys):
    """
    Returns a formatted string with details about the error,
    including the file name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script [{0}] at line [{1}]: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    """
    Custom exception class for enhanced error logging and readability.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
        logging.error(self.error_message)  # Optional: automatically logs the error

    def __str__(self):
        
        return self.error_message
