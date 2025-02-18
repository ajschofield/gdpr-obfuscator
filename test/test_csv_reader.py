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
        Bucket=bucket,
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


def test_read_s3_empty_csv_returns_empty_list():
    with mock_aws():
        s3 = boto3.client("s3", region_name="eu-west-2")
        bucket = "empty-bucket"
        key = "data/empty.csv"
        csv_content = "student_id,name,course\n"
        setup_s3(s3, bucket, key, csv_content)
        path = f"s3://{bucket}/{key}"

        data = CSVReader.read_s3(path)
        assert data == []


def test_read_s3_nonexistent_bucket_raises_exception():
    with mock_aws():
        bucket = "nonexistent-bucket"
        key = "data/mock.csv"
        path = f"s3://{bucket}/{key}"
        with pytest.raises(Exception):
            CSVReader.read_s3(path)


def test_read_s3_nonexistent_key_raises_exception():
    with mock_aws():
        s3 = boto3.client("s3", region_name="eu-west-2")
        bucket = "test-bucket"
        s3.create_bucket(
            Bucket=bucket,
            CreateBucketConfiguration={"LocationConstraint": "eu-west-2"},
        )
        key = "data/nonexistent.csv"
        path = f"s3://{bucket}/{key}"
        with pytest.raises(Exception):
            CSVReader.read_s3(path)


def test_read_s3_malformed_csv_returns_expected():
    with mock_aws():
        s3 = boto3.client("s3", region_name="eu-west-2")
        bucket = "test-bucket"
        key = "data/malformed.csv"
        csv_content = "1234,Student 1,Course 1\n" "5678,Student 2,Course 2\n"
        setup_s3(s3, bucket, key, csv_content)
        path = f"s3://{bucket}/{key}"

        data = CSVReader.read_s3(path)
        expected = [{"1234": "5678", "Student 1": "Student 2", "Course 1": "Course 2"}]
        assert data == expected


def test_read_s3_csv_with_extra_empty_lines():
    with mock_aws():
        s3 = boto3.client("s3", region_name="eu-west-2")
        bucket = "test-bucket"
        key = "data/extra_lines.csv"
        csv_content = (
            "student_id,name,course\n"
            "1234,Student 1,Course 1\n"
            "\n"
            "5678,Student 2,Course 2\n"
            "\n"
        )
        setup_s3(s3, bucket, key, csv_content)
        path = f"s3://{bucket}/{key}"

        data = CSVReader.read_s3(path)
        expected = [
            {"student_id": "1234", "name": "Student 1", "course": "Course 1"},
            {"student_id": "5678", "name": "Student 2", "course": "Course 2"},
        ]
        assert data == expected


def test_read_s3_csv_with_whitespace_in_fields():
    with mock_aws():
        s3 = boto3.client("s3", region_name="eu-west-2")
        bucket = "test-bucket"
        key = "data/whitespace.csv"
        csv_content = (
            "student_id, name , course \n"
            " 1234 , Student 1 , Course 1 \n"
            "5678,Student 2,Course 2\n"
        )
        setup_s3(s3, bucket, key, csv_content)
        path = f"s3://{bucket}/{key}"

        data = CSVReader.read_s3(path)
        expected = [
            {"student_id": " 1234 ", " name ": " Student 1 ", " course ": " Course 1 "},
            {"student_id": "5678", " name ": "Student 2", " course ": "Course 2"},
        ]
        assert data == expected
