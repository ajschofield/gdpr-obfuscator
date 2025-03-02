from .read import FileHandler
from .obfuscate import obfuscate_data
from .utils import Utilities


class Obfuscator:
    """
    Provides the functionality to obfuscate the sensitive PII data in CSV files.

    It integrates the file handler to load the CSV data and the obfuscation logic to
    replace the PII fields with obfuscated values. The obfuscated data is then returned
    as a byte stream.

    The input is expected to be a JSON string containing the file path and the PII fields,
    and the user should utilise either the `process_s3` or `process_local` methods to
    obfuscate the data, depending on the file location.
    """

    def __init__(self):
        """
        Initialise the Obfuscator with a FileHandler and Utilities instance.
        """
        self.reader = FileHandler()
        self.utils = Utilities()

    def process_s3(self, input: str) -> bytes:
        """
        Process a CSV file stored in an S3 bucket and obfuscate the PII fields.

        The method expects a JSON string input that contains:
        - "file_path": an S3 URI (e.g., "s3://bucket/key")
        - "pii_fields": a list of column names that contain PII

        Args:
            input (str): A JSON string containing the S3 URI and PII fields, respectively

        Returns:
            bytes: The obfuscated CSV data as a byte stream
        """

        path, pii_fields = self.utils.process_json_input(input)
        obfuscated_data = obfuscate_data(self.reader.read_s3(path), pii_fields)
        return self.utils.create_byte_stream(obfuscated_data)

    def process_local(self, input: str) -> bytes:
        """
        Process a CSV file stored locally and obfuscate the PII fields.

        The method expects a JSON string input that contains:
        - "file_path": a local file path
        - "pii_fields": a list of column names that contain PII

        NOTE: Since the scope of the project is to obfuscate data stored in S3, this method
        has only been tested to work on MacOS and Linux systems.

        Args:
            input (str): A JSON string containing the local file path and PII fields, respectively

        Returns:
            bytes: The obfuscated CSV data as a byte stream
        """

        path, pii_fields = self.utils.process_json_input(input)
        obfuscated_data = obfuscate_data(self.reader.read_local(path), pii_fields)
        return self.utils.create_byte_stream(obfuscated_data)
