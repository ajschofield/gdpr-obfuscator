import csv
import io
from enum import Enum
from typing import List, Dict
import json


class Utilities:

    def process_json_input(json_input: str):
        data = json.loads(json_input)

        if not data.get("file_path") or not data.get("pii_fields"):
            raise ValueError(
                "Missing required file_path & pii_fields entries in JSON input"
            )

        return data["file_path"], data["pii_fields"]

    @staticmethod
    def get_s3_path(uri):
        parts = uri.replace("s3://", "").split("/")
        bucket = parts.pop(0)
        key = "/".join(parts)
        return bucket, key

    @staticmethod
    def create_byte_stream(data: List[Dict[str, str]]) -> bytes:
        if not data:
            return b""

        output = io.StringIO()

        headers = list(data[0].keys())

        writer = csv.DictWriter(output, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

        csv_string = output.getvalue()

        return csv_string.encode("utf-8")
