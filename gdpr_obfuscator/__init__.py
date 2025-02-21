from .read import DataReader
from .obfuscate import obfuscate_data
from typing import List, Dict


class Obfuscator:
    def __init__(self):
        self.reader = DataReader()

    def process_s3(self, path: str, pii_fields: List[str]) -> bytes:
        return obfuscate_data(self.reader.read_s3(path), pii_fields)

    def process_local(self, path: str, pii_fields: List[str]) -> bytes:
        return obfuscate_data(self.reader.read_local(path), pii_fields)
