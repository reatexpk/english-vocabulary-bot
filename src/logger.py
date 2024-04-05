import os
import logging

LOGS_DIR = 'logs'


def init_logger():
    if not os.path.isdir(LOGS_DIR):
        os.mkdir(LOGS_DIR)
    log_file = os.path.join(os.getcwd(), LOGS_DIR, 'bot.log')
    print("Logging to", log_file)
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] %(levelname)s : %(message)s',
        filename=log_file,
        filemode='a',
    )
