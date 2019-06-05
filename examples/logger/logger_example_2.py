
import logging

log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger("my logger_examp_2")
logger.setLevel(logging.DEBUG)

f_handler = logging.FileHandler('loggerexample2.log')
f_handler.setLevel(logging.DEBUG)


f_handler.setFormatter(log_format)

logger.addHandler(f_handler)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARN)
stream_handler.setFormatter(log_format)

logger.addHandler(stream_handler)


logger.debug("test")

def fun_use_logger():
    logger.debug("test 2 debug")
    # Only this will be displayed to console
    logger.error("test 3 error")

fun_use_logger()