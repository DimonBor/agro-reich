import logging


def get_logger(thread_name):
    logger = logging.getLogger(thread_name)
    if not logger.hasHandlers():
        match thread_name:
            case "MainThread":
                logger.setLevel(logging.INFO)
            case "CordsUpdater":
                logger.setLevel(logging.INFO)
            case _:
                logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
            )

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)

    return logger
