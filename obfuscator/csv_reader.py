import csv
from typing import List, Dict
from obfuscator.logger import get_logger

logger = get_logger("CSVReader")

class CSVReader:
    def __init__(self):
        pass

    def read_local(self, path) -> List[Dict[str, str]]:
        logger.debug(f"Reading local CSV from: {path}")
        data = []

        try:
            with open(path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(dict(row))
        except FileNotFoundError:
            logger.error(f"File not found: {path}")
        except Exception as e:
            logger.error(f"Error reading file: {e}")

        logger.debug(f"Total rows read: {len(data)}")
        return data

    def read_s3(self) -> List[Dict[str, str]]:
        return []



