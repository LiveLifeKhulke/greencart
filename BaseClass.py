import logging

import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getlogger(self):
        logger=logging.getLogger(__name__)
        filehandler=logging.FileHandler("logging.log")
        formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger