from typing import List, Dict
from obfuscator.logger import get_logger

# Create the logger
logger = get_logger("Obfuscator")

def obfuscate(
    data: List[Dict[str, str]], pii_fields: List[str]
) -> List[Dict[str, str]]:
    """
    A function to obfuscate PII fields in a list of dictionaries, replacing
    sensitive values with a string of asterisks.
    """
    # If no data is provided, log a message and return an empty list
    if not data:
        logger.info("No valid data was provided to obfuscate")
        return []

    # Obfuscate the PII fields in each record using a list/dict comprehension
    # This code is good but makes debugging a bit tricky. I may consider
    # breaking it down into a for loop.
    return [
        {k: ("***" if k in pii_fields else v) for k, v in record.items()}
        for record in data
    ]
