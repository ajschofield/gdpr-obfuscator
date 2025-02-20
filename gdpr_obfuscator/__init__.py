from .read import DataReader
from .write import DataWriter
from .obfuscate import obfuscate
from typing import List


def main(s3_source: str, pii_fields: List[str], log_level: str = "INFO") -> bytes:
    reader = DataReader(log_level)
    writer = DataWriter()
    data = reader.read_s3(s3_source)
    obfuscated_data = obfuscate(data, pii_fields)
    return writer.create_byte_stream(obfuscated_data)
