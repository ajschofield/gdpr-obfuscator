from read import DataReader
from write import DataWriter
from utils import Utilities
from obfuscate import obfuscate
from types import List


def main(s3_source: str, pii_fields: List[str], log_level: str = "INFO") -> bytes:
    reader = DataReader(log_level)
    writer = DataWriter()
    utilities = Utilities()
    source = utilities.get_source(s3_source)
    data = reader.read_string(source)
    obfuscated_data = obfuscate(data, pii_fields)
    return writer.create_byte_stream(obfuscated_data)
