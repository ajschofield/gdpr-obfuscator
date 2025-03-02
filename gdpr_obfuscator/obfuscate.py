from typing import List, Dict


def obfuscate_data(
    data: List[Dict[str, str]], pii_fields: List[str]
) -> List[Dict[str, str]]:
    """


    Args:
        data (List[Dict[str, str]]): _description_
        pii_fields (List[str]): _description_

    Raises:
        ValueError: _description_

    Returns:
        List[Dict[str, str]]: _description_
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
