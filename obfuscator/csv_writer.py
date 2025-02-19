import csv
import io
from typing import List, Dict
from obfuscator.logger import get_logger

# Create the logger
logger = get_logger("CSVWRITER")


def create_byte_stream(data: List[Dict[str, str]]) -> bytes:
    if not data:
        logger.info("No valid data was provided to write")
        return b""

    output = io.StringIO()

    headers = list(data[0].keys())

    writer = csv.DictWriter(output, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

    csv_string = output.getvalue()
    logger.debug(f"CSV data: {csv_string}")

    return csv_string.encode("utf-8")
