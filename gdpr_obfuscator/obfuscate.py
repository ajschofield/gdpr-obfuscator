from typing import List, Dict


def obfuscate_data(
    data: List[Dict[str, str]], pii_fields: List[str]
) -> List[Dict[str, str]]:
    """
    A function to obfuscate PII fields in a list of dictionaries, replacing
    sensitive values with a string of asterisks.
    """

    return [
        {k: ("***" if k in pii_fields else v) for k, v in record.items()}
        for record in data
    ]
