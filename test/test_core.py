from gdpr_obfuscator import Obfuscator
import pytest
from moto import mock_aws
import boto3
import csv
import random

obfuscator = Obfuscator()


def setup_s3(s3_client, bucket: str, key: str, content: str):
    s3_client.create_bucket(
        Bucket=bucket,
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )
    s3_client.put_object(Bucket=bucket, Key=key, Body=content)


@pytest.fixture(autouse=True)
def s3_client():
    with mock_aws():
        yield boto3.client("s3", "eu-west-2")


def test_main_integration():
    with mock_aws():
        s3 = boto3.client("s3", region_name="eu-west-2")
        bucket = "test-bucket"
        key = "data/mock.csv"

        with open("test/data/mock_data.csv", "r") as f:
            csv_content = f.read()

        with open("test/data/mock_data.csv", "r") as f:
            reader = list(csv.DictReader(f))
            rand_row = random.randint(0, len(reader) - 1)
            rand_name = reader[rand_row]["name"]

        setup_s3(s3, bucket, key, csv_content)

        path = f"s3://{bucket}/{key}"

    result = obfuscator.process_s3(path, ["name"])
    result_str = result.decode("utf-8")

    assert rand_name not in result_str
