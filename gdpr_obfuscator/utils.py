import csv
import io
from typing import List, Dict, Tuple
import json


class Utilities:
    @staticmethod
    def process_json_input(json_input: str) -> Tuple[str, List[str]]:
        """
        Parse JSON input and return the file path and PII fields.

        The JSON string is required to have:
        - file_path: the path to the file to be processed
        - pii_fields: a list of fields to be obfuscated

        Args:
            json_input (str): A JSON string containing the file path and PII fields

        Raises:
            ValueError: If the JSON input is missing "file_path" or "pii_fields"

        Returns:
            Tuple[str, List[str]]: A tuple containing the file path and PII fields, respectively
        """

        data = json.loads(json_input)

        if not data.get("file_path") or not data.get("pii_fields"):
            raise ValueError(
                "Missing required file_path & pii_fields entries in JSON input"
            )

        return data["file_path"], data["pii_fields"]

    @staticmethod
    def get_s3_path(uri) -> Tuple[str, str]:
        """
        Extract the S3 bucket name and key from a given S3 URI.

        Args:
            uri (_type_): The S3 URI to extract the bucket and key from

        Returns:
            Tuple[str, str]: A tuple containing the bucket name and the key, respectively
        """

        parts = uri.replace("s3://", "").split("/")
        bucket = parts.pop(0)
        key = "/".join(parts)
        return bucket, key

    @staticmethod
    def create_byte_stream(data: List[Dict[str, str]]) -> bytes:
        """
        Convert a list of dictionaries (representing CSV rows) into a CSV byte stream.

        If the input data is empty, an empty byte stream is returned.

        Args:
            data (List[Dict[str, str]]): A list of dictionaries representing CSV rows

        Returns:
            bytes: A byte stream representing the CSV data
        """
        if not data:
            return b""

        output = io.StringIO()

        headers = list(data[0].keys())

        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

        csv_string = output.getvalue()

        return csv_string.encode("utf-8")
