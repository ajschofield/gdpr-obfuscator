import csv
import io
import logging
import Enum
from typing import List, Dict


class Utilities:
    class LogLevel(Enum):
        DEBUG = logging.DEBUG
        INFO = logging.INFO
        WARNING = logging.WARNING
        ERROR = logging.ERROR
        CRITICAL = logging.CRITICAL

    @staticmethod
    def get_logger(name: str, level: "Utilities.LogLevel" = None) -> logging.Logger:
        level = level or Utilities.LogLevel.INFO
        logger = logging.getLogger(name)
        if logger.hasHandlers():
            logger.handlers.clear()

        handler = logging.StreamHandler()
        logger.setLevel(level.value)
        formatter = logging.Formatter(
            "[%(asctime)s] - %(levelname)s::%(name)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def __init__(self, logger=None):
        self.logger = self.get_logger(__name__, logger)

    def get_s3_path(self, uri):
        parts = uri.replace("s3://", "").split("/")
        self.logger.debug(f"Parts: {parts}")
        bucket = parts.pop(0)
        self.logger.debug(f"Bucket: {bucket}")
        key = "/".join(parts)
        self.logger.debug(f"Key: {key}")
        return bucket, key

    def create_byte_stream(self, data: List[Dict[str, str]]) -> bytes:
        if not data:
            self.logger.error("Invalid or empty data was provided to write")
            return b""

        output = io.StringIO()

        headers = list(data[0].keys())

        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

        csv_string = output.getvalue()

        return csv_string.encode("utf-8")
