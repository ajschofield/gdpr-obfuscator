import csv
import io
from typing import List, Dict
from obfuscator.logger import get_logger

logger = get_logger("CSVReader")

class CSVReader:
    @staticmethod
    def read_local(path) -> List[Dict[str, str]]:
        logger.debug(f"Reading local CSV from: {path}")

        try:
            with open(path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return [dict(row) for row in reader]
        except FileNotFoundError:
            logger.error(f"File not found: {path}")
        except Exception as e:
            logger.error(f"Error reading file: {e}")
    
    @staticmethod
    def read_s3(path) -> List[Dict[str, str]]:
        return []

    @staticmethod
    def read_string(content: str) -> List[Dict[str, str]]:
        if not content.strip():
            return []
        
        f = io.StringIO(content)
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]
