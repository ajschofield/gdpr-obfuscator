# Utility functions
from obfuscator.logger import get_logger

# Create the logger
logger = get_logger("CLI")


def get_s3_path(uri):
    parts = uri.replace("s3://", "").split("/")
    logger.debug(f"Parts: {parts}")
    bucket = parts.pop(0)
    logger.debug(f"Bucket: {bucket}")
    key = "/".join(parts)
    logger.debug(f"Key: {key}")
    return bucket, key
