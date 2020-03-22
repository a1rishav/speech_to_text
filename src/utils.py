import logging
from logging.handlers import TimedRotatingFileHandler
import os
from application_properties import ApplicationProperties as props

def create_dir_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path, exist_ok=True)

def init_logger(module, logging_level=logging.DEBUG):
    create_dir_if_not_exists(props.logs_dir)
    logger = logging.getLogger(module)
    logger.setLevel(logging_level)
    logname = os.path.join(props.logs_dir, "app.log")
    rotation_handler = TimedRotatingFileHandler(logname, when="midnight", interval=1)
    rotation_handler.suffix = "%Y-%m-%d"
    rotation_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s")
    rotation_handler.setFormatter(formatter)
    logger.addHandler(rotation_handler)
    return logger

