import csv
import io
import boto3
import os
from typing import List, Dict
from obfuscator.logger import get_logger
from obfuscator.utils import Utilities


class CSVReader:
    """
    A class to read CSV data from a local file, S3 object, or string. Near
    the project completion, support for JSON/Parquet files will be added.
    """

    def __init__(self, log_level=None):
        self.log_level = log_level
        self.logger = get_logger("CSVREADER", log_level)

    def read_local(self, path) -> List[Dict[str, str]]:
        """
        A method to read a local CSV file and return the data as a list of
        dictionaries.
        """
        self.logger.debug(f"Reading local CSV from: {path}")

        try:
            with open(path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return [dict(row) for row in reader]
        except FileNotFoundError:
            self.logger.error(f"File not found: {path}")
            raise
        except Exception as e:
            self.logger.error(f"Error reading file: {e}")

    def read_s3(self, path) -> List[Dict[str, str]]:
        """
        A method to read an S3 object containing CSV data
        and return the data as a list of dictionaries.
        """
        utils = Utilities(self.log_level)
        bucket, key = utils.get_s3_path(path)
        self.logger.debug(f"Reading S3 CSV from: {bucket}/{key}")

        if os.getenv("LOCALSTACK", "FALSE").upper() == "TRUE":
            localstack_endpoint = "http://localhost.localstack.cloud:4566"
            self.logger.debug("Using LocalStack endpoint for S3")
            client = boto3.client(
                "s3",
                endpoint_url=localstack_endpoint,
                aws_access_key_id="dummy",
                aws_secret_access_key="dummy",
            )
            self.logger.debug(f"endpoint_url: {localstack_endpoint}")
        else:
            client = boto3.client("s3")

        try:
            response = client.get_object(Bucket=bucket, Key=key)
            self.logger.info("S3 object read successfully")
            content = response["Body"].read().decode("utf-8")
            return CSVReader.read_string(content)
        except Exception as e:
            self.logger.error(f"Error reading S3 object: {e}")
            raise

    def read_string(self, content: str) -> List[Dict[str, str]]:
        """
        A method to read CSV data from a string and return the data as a list
        of dictionaries.
        """
        if not content.strip():
            return []

        f = io.StringIO(content)
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]
