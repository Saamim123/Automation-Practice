# utilities/customlogger.py
import logging
import os
from datetime import datetime
import sys


class LogGen:
    @staticmethod
    def loggen():
        try:
            # Get the root directory of the project
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            log_dir = os.path.join(project_root, 'logs')

            # Create logs directory if it doesn't exist
            os.makedirs(log_dir, exist_ok=True)

            # Create log file name with timestamp
            log_file = os.path.join(log_dir, f'automation.log')

            # Create logger
            logger = logging.getLogger('automation')
            logger.setLevel(logging.INFO)

            # Clear existing handlers to avoid duplicate logs
            if logger.hasHandlers():
                logger.handlers.clear()

            # Create file handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.INFO)

            # Create console handler
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.INFO)

            # Create formatter and add it to the handlers
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                          datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add the handlers to the logger
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

            logger.info("Logger successfully initialized")
            return logger

        except Exception as e:
            print(f"Failed to initialize logger: {str(e)}")
            raise