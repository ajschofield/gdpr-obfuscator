# Utility functions
from .logger import get_logger
from typing import List, Dict
import csv
import io


class Utilities:
    def __init__(self, logger=None):
        self.logger = get_logger("UTILITIES", logger)

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
