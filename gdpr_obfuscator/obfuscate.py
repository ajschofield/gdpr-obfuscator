from typing import List, Dict


def obfuscate_data(
    data: List[Dict[str, str]], pii_fields: List[str]
) -> List[Dict[str, str]]:
    """
    A function to obfuscate PII fields in a list of dictionaries, replacing
    sensitive values with a string of asterisks.
    """

    for record in data:
        missing_pii_fields = [field for field in pii_fields if field not in record]
        if missing_pii_fields:
            raise ValueError(
                f"A record is missing required PII fields: {missing_pii_fields}"
            )

    return [
        {k: ("***" if k in pii_fields else v) for k, v in record.items()}
        for record in data
    ]
