# Utility functions
from obfuscator.logger import get_logger


class Utilities:

    def __init__(self, logger=None):
        # Create the logger
        self.logger = get_logger("UTILITIES", logger)

    def get_s3_path(self, uri):
        parts = uri.replace("s3://", "").split("/")
        self.logger.debug(f"Parts: {parts}")
        bucket = parts.pop(0)
        self.logger.debug(f"Bucket: {bucket}")
        key = "/".join(parts)
        self.logger.debug(f"Key: {key}")
        return bucket, key
