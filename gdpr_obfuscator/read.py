import csv
import io
import boto3
from typing import List, Dict
from .utils import Utilities


class FileHandler:
    """
    A class to read CSV data from a local file, S3 object, or string. Currently,
    CSV files are supported but support for JSON and Parquet files may be
    added in the future.
    """

    def __init__(self):
        """
        Initialise the FileHandler with a Utilities instance.
        """
        self.utils = Utilities()

    def read_local(self, file_path) -> List[Dict[str, str]]:
        """
        Read a local CSV file and return the data as a list of dictionaries.

        The file path should be a local path to the CSV file. There is no logic
        to convert file paths between operating systems since `read_s3` is the
        main method to be used. Therefore, this method will only work reliably
        on MacOS and Linux systems.

        This method uses the built-in `open` function to read the CSV file and
        then reads the CSV data using `read_string` to be returned.

        Args:
            file_path (_type_): The local file path to the CSV file

        Returns:
            List[Dict[str, str]]: A list of dictionaries representing the CSV data rows
        """

        with open(file_path, mode="r", encoding="utf-8") as f:
            return self.read_string(f.read())

    def read_s3(self, file_path) -> List[Dict[str, str]]:
        """
        Read a CSV file within an S3 bucket and return the data as a list of dictionaries.

        The S3 URI should be in the format "s3://bucket/key". This method uses
        get_object present in the boto3 library to interact with S3 and retrieve
        the CSV file. Once retrieved, the CSV data is read using `read_string`
        and is returned.

        Args:
            file_path (_type_): The local file path to the CSV file

        Returns:
            List[Dict[str, str]]: A list of dictionaries representing the CSV data rows
        """
        bucket, key = self.utils.get_s3_path(file_path)

        client = boto3.client("s3")

        response = client.get_object(Bucket=bucket, Key=key)
        content = response["Body"].read().decode("utf-8")
        read_csv_content = self.read_string(content)
        return read_csv_content

    @staticmethod
    def read_string(content: str) -> List[Dict[str, str]]:
        """
        Parse raw data provided by read helpers and return the data as a list of dictionaries.

        If the provided string is empty, an empty list is returned.

        Args:
            content (str): The raw CSV data as a string

        Returns:
            List[Dict[str, str]]: A list of dictionaries representing the CSV data rows
        """
        if not content.strip():
            return []

        f = io.StringIO(content)
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]
