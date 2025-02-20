from .read import DataReader
from .obfuscate import obfuscate
from .logger import get_logger
from typing import List, Dict

class ImportData:
    def __init__(self, verbosity: bool = False):
        self.verbosity = verbosity
        self.log_level = "DEBUG" if verbosity else "INFO"
        self.logger = get_logger("ImportData", self.log_level)
        self.reader = DataReader()

    def import_s3(self, path: str, pii_fields: List[str]) -> bytes:
        return self.reader.read_s3(path)

    def import_local(self, path: str, pii_fields: List[str]) -> bytes:
        return self.reader.read_local(path)