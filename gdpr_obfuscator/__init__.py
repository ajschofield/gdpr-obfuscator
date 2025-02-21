from .read import DataReader
from .obfuscate import obfuscate
from typing import List, Dict


class Obfuscator:
    def __init__(self):
        self.reader = DataReader()

    def import_s3(self, path: str, pii_fields: List[str]) -> bytes:
        return self.reader.read_s3(path)

    def import_local(self, path: str, pii_fields: List[str]) -> bytes:
        return self.reader.read_local(path)
