# csv_reader.py - tests
# Author: Alex Schofield

import boto3
from moto import mock_aws
from obfuscator.csv_reader import CSVReader
import pytest

reader = CSVReader()

# CSVREADER: READ_STRING TESTS

# Check if the function can read a CSV string with no content and return
# an empty list


def test_empty_csv_should_return_no_content():
    content = ""
    result = reader.read_string(content)
    expected = []
    assert result == expected


# Check if the function can read a CSV string with only a header and return
# an empty list


def test_csv_with_header_only_should_return_no_content():
    content = "student_id,name,course\n"
    result = reader.read_string(content)
    expected = []
    assert result == expected


# Check if the function can read a CSV string with valid data and return
# a list of dictionaries


def test_csv_with_valid_data():
    content = (
        "student_id,name,course\n"
        "1234,Student 1,Course 1\n"
        "5678,Student 2,Course 2\n"
    )
    result = reader.read_string(content)
    expected = [
        {"student_id": "1234", "name": "Student 1", "course": "Course 1"},
        {"student_id": "5678", "name": "Student 2", "course": "Course 2"},
    ]
    assert result == expected


# Check if the function can read a CSV string with quoted fields and return
# a list of dictionaries with the quoted fields intact


def test_csv_with_quoted_fields_should_run_as_expected():
    content = (
        "student_id,name,course\n"
        '1234,"Student 1","Course 1"\n'
        '5678,"Student 2","Course 2"\n'
    )
    result = reader.read_string(content)
    expected = [
        {"student_id": "1234", "name": "Student 1", "course": "Course 1"},
        {"student_id": "5678", "name": "Student 2", "course": "Course 2"},
    ]
    assert result == expected


# CSVREADER: READ_S3 TESTS


def setup_s3(s3_client, bucket: str, key: str, content: str):
    s3_client.create_bucket(
        Bucket="test-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
    )
    s3_client.put_object(Bucket=bucket, Key=key, Body=content)


@pytest.fixture(autouse=True)
def s3_client():
    with mock_aws():
        yield boto3.client("s3", "eu-west-2")


def test_read_s3_valid_csv_returns_expected():
    with mock_aws():
        s3 = boto3.client("s3", region_name="eu-west-2")
        bucket = "test-bucket"
        key = "data/mock.csv"

        csv_content = (
            "student_id,name,course\n"
            "1234,Student 1,Course 1\n"
            "5678,Student 2,Course 2\n"
        )

        setup_s3(s3, bucket, key, csv_content)
        path = f"s3://{bucket}/{key}"

        data = reader.read_s3(path)

        expected = [
            {"student_id": "1234", "name": "Student 1", "course": "Course 1"},
            {"student_id": "5678", "name": "Student 2", "course": "Course 2"},
        ]

        assert data == expected
