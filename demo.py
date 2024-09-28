from us_visa.logger import logging
from us_visa.exception import USVisaException
import sys


logging.info("Working with custom exceptions")

try:
    2/0
except Exception as e:
    raise USVisaException(e, sys)

