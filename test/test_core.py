from gdpr_obfuscator import Obfuscator
import pytest
from moto import mock_aws
import boto3
import csv
import random
import json
import time

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


def test_imported_module_runs_successfully_with_local_data():
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

    json_input = json.dumps({"file_path": path, "pii_fields": ["name"]})

    result = obfuscator.process_s3(json_input)
    result_str = result.decode("utf-8")

    assert rand_name not in result_str


def test_imported_module_completes_in_under_one_minute():
    with mock_aws():
        s3 = boto3.client("s3", region_name="eu-west-2")
        bucket = "test-bucket"
        key = "data/large_dataset.csv"

        with open("test/data/large_dataset.csv", "r") as f:
            csv_content = f.read()

        setup_s3(s3, bucket, key, csv_content)

        path = f"s3://{bucket}/{key}"

    json_input = json.dumps(
        {"file_path": path, "pii_fields": ["full_name", "email_address"]}
    )

    start = time.time()
    obfuscator.process_s3(json_input)
    end = time.time()

    assert end - start < 60


def test_output_compatible_with_s3_put_object():
    with mock_aws():
        s3 = boto3.client("s3", region_name="eu-west-2")
        bucket = "test-bucket"
        key = "data/mock.csv"
        output_key = "data/obfuscated.csv"

        with open("test/data/mock_data.csv", "r") as f:
            csv_content = f.read()

        setup_s3(s3, bucket, key, csv_content)
        path = f"s3://{bucket}/{key}"

        json_input = json.dumps({"file_path": path, "pii_fields": ["name"]})
        result_bytes = obfuscator.process_s3(json_input)

        try:
            response = s3.put_object(Bucket=bucket, Key=output_key, Body=result_bytes)
            assert response["ResponseMetadata"]["HTTPStatusCode"] == 200

            get_response = s3.get_object(Bucket=bucket, Key=output_key)
            retrieved_content = get_response["Body"].read()

            assert retrieved_content == result_bytes

        # Shouldn't reach this point but catch and fail anyway

        except Exception as e:
            pytest.fail(f"put_object did not like the output from process_s3: {e}")
