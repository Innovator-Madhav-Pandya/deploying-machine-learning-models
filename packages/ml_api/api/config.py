logger = logging.getLogger(logger_name)

logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

logger.addHandler(get_console_handler())
logger.addHandler(get_file_handler())
