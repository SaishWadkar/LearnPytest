import logging

logging.basicConfig(filename="test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p'
                    )

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Debug")
logger.info("Info")

logger.warning("Warning")
logger.error("Error")
logger.critical("Critical")