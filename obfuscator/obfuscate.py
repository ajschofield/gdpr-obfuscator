from typing import List, Dict
from obfuscator.logger import get_logger

logger = get_logger("Obfuscator")


def obfuscate(
    data: List[Dict[str, str]], pii_fields: List[str]
) -> List[Dict[str, str]]:
    if not data:
        logger.info("No valid data was provided to obfuscate")
        return []

    return [
        {k: ("***" if k in pii_fields else v) for k, v in record.items()}
        for record in data
    ]
