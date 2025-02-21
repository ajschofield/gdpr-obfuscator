from .read import DataReader
from .obfuscate import obfuscate
from typing import List, Dict
from .utils import Utilities


class Obfuscator:
    def __init__(self, verbosity: bool = False):
        self.verbosity = verbosity
        self.log_level = "DEBUG" if verbosity else "INFO"
        self.logger = Utilities.get_logger("ImportData", self.log_level)
        self.reader = DataReader()

    def import_s3(self, path: str, pii_fields: List[str]) -> bytes:
        return self.reader.read_s3(path)

    def import_local(self, path: str, pii_fields: List[str]) -> bytes:
        return self.reader.read_local(path)
