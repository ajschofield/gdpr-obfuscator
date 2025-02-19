from typing import List, Dict
from obfuscator.logger import get_logger

logger = get_logger("OBFUSCATE")


def obfuscate(
    data: List[Dict[str, str]], pii_fields: List[str]
) -> List[Dict[str, str]]:
    """
    A function to obfuscate PII fields in a list of dictionaries, replacing
    sensitive values with a string of asterisks.
    """
    if not data:
        logger.error("Invalid or empty was provided to obfuscate")
        raise ValueError("Invalid data provided to obfuscate")
    if not pii_fields:
        logger.error("No PII fields provided to obfuscate")
        raise ValueError("No PII fields provided to obfuscate")

    return [
        {k: ("***" if k in pii_fields else v) for k, v in record.items()}
        for record in data
    ]
