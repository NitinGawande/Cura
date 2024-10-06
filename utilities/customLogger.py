import logging
import os
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(
#         filename=".\\Log\\automation.log",  # Log file name
#         format='%(asctime)s - %(levelname)s - %(message)s',
#         datefmt='%Y-%m-%d %H:%M:%S')
#
#         logger=logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger

# class LogGen:
#
#     @staticmethod
#     def loggen():
#
#         logging.basicConfig(
#         level=logging.DEBUG,  # Set the log level
#         format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
#         handlers=[
#         logging.FileHandler('Log/application.log'),  # Log to file in Logs folder
#         logging.StreamHandler()  # Log to console
#     ]
# )
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger
import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Create Logs directory if it doesn't exist
        log_dir = "Log"  # Change this to your desired directory
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create a logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)  # Set the log level

        # Create file handler
        file_handler = logging.FileHandler(os.path.join(log_dir, "automation.log"))
        file_handler.setLevel(logging.INFO)  # Set level for file handler

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Set level for console handler

        # Define the format for the handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # Set the formatter for the handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
