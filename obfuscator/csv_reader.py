import csv
from io import StringIO
from typing import List, Dict
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def read_local(content: str) -> List[Dict[str, str]]:
    f = StringIO(content)
    reader = csv.DictReader(f)
    logger.info("Finished reading CSV!")
    return list(reader)

def read_s3():
    pass


