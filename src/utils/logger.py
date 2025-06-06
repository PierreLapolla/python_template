import logging

import structlog

LOG_LEVEL = logging.DEBUG

structlog.configure(wrapper_class=structlog.make_filtering_bound_logger(LOG_LEVEL))

log = structlog.get_logger()

if __name__ == "__main__":
    """
    Example usage of the logger.
    """
    log.debug("Debug message")
    log.info("Info message")
    log.warning("Warning message")
    log.error("Error message")
    log.critical("Critical message")
