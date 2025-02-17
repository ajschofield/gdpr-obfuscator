import csv
import io
from typing import List, Dict
from obfuscator.logger import get_logger

# Create the logger
logger = get_logger("CSVReader")

# Putting the CSV reading components into a class may seem like overkill
# for a simple script, but it allows for better organization and scalability.
# @staticmethod is used to define the method without an instance of the class
# being required. The methods could be defined just as functions, and this
# may still be changed.


class CSVReader:
    """
    A class to read CSV data from a local file, S3 object, or string. Near
    the project completion, support for JSON/Parquet files will be added.
    """

    @staticmethod
    def read_local(path) -> List[Dict[str, str]]:
        """
        A method to read a local CSV file and return the data as a list of
        dictionaries.
        """
        # Log the path of the file being read for debugging
        logger.debug(f"Reading local CSV from: {path}")

        # Attempt to read the file and return the data as a list of dictionaries
        # However, if the file isn't found or there is a generic exception, log
        # the error and raise an exception
        try:
            with open(path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return [dict(row) for row in reader]
        except FileNotFoundError:
            logger.error(f"File not found: {path}")
            raise
        except Exception as e:
            logger.error(f"Error reading file: {e}")

    @staticmethod
    def read_s3(path) -> List[Dict[str, str]]:
        """
        A method to read an S3 object containing CSV data
        and return the data as a list of dictionaries.
        """
        # Yet to be implemented.
        return []

    @staticmethod
    def read_string(content: str) -> List[Dict[str, str]]:
        """
        A method to read CSV data from a string and return the data as a list
        of dictionaries.
        """
        # If the content is empty, return an empty list
        if not content.strip():
            return []

        # Treat the string as a file-like object and return as list of dictionaries
        f = io.StringIO(content)
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]
