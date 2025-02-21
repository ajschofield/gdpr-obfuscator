import csv
import io
import boto3
from typing import List, Dict
from .utils import Utilities


class DataReader:
    """
    A class to read CSV data from a local file, S3 object, or string. Near
    the project completion, support for JSON/Parquet files will be added.
    """

    def __init__(self):
        self.utils = Utilities()

    def read_local(self, path) -> List[Dict[str, str]]:
        """
        A method to read a local CSV file and return the data as a list of
        dictionaries.
        """

        with open(path, mode="r", encoding="utf-8") as f:
            return self.read_string(f.read())

    def read_s3(self, path) -> List[Dict[str, str]]:
        """
        A method to read an S3 object containing CSV data
        and return the data as a list of dictionaries.
        """
        bucket, key = self.utils.get_s3_path(path)

        client = boto3.client("s3")

        response = client.get_object(Bucket=bucket, Key=key)
        content = response["Body"].read().decode("utf-8")
        read_csv_content = self.read_string(content)
        return read_csv_content

    @staticmethod
    def read_string(content: str) -> List[Dict[str, str]]:
        """
        A method to read CSV data from a string and return the data as a list
        of dictionaries.
        """
        if not content.strip():
            return []

        f = io.StringIO(content)
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]
