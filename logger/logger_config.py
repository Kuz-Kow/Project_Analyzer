import logging
from logging.handlers import RotatingFileHandler 

def set_logger() -> None:
    logger = logging.getLogger()
    logger.setLevel("INFO")
    file_formatter = logging.Formatter(fmt= "{asctime} - {name} - {levelname}: {message}", style="{", datefmt="%Y-%m-%d %H:%M:%S")
    cls_formatter = logging.Formatter(fmt= "{name} - {levelname}: {message}", style="{")
    
    
    file_handler = RotatingFileHandler(filename= "reports/analyzer.logs", mode= "a", maxBytes="1000",backupCount=10,encoding="utf-8")
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel("INFO")
    
    cls_handler = logging.StreamHandler()
    cls_handler.setFormatter(cls_formatter)
    cls_handler.setLevel("ERROR")