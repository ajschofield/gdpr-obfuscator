from .read import DataReader
from .obfuscate import obfuscate_data
from .utils import Utilities
from typing import List


class Obfuscator:
    def __init__(self):
        self.reader = DataReader()
        self.utils = Utilities()

    def process_s3(self, input: str) -> bytes:
        path, pii_fields = self.utils.process_json_input(input)
        obfuscated_data = obfuscate_data(self.reader.read_s3(path), pii_fields)
        return self.utils.create_byte_stream(obfuscated_data)

    def process_local(self, input: str) -> bytes:
        path, pii_fields = self.utils.process_json_input(input)
        obfuscated_data = obfuscate_data(self.reader.read_local(path), pii_fields)
        return self.utils.create_byte_stream(obfuscated_data)
