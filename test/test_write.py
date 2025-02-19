import io
import csv
from obfuscator.write import create_byte_stream


def csv_bytes_to_list(csv_bytes: bytes):
    csv_string = csv_bytes.decode("utf-8")
    f = io.StringIO(csv_string)
    reader = csv.DictReader(f)
    return [dict(row) for row in reader]


def test_create_byte_stream_valid_data():
    data = [
        {"student_id": "1234", "name": "Student 1", "course": "Course 1"},
        {"student_id": "5678", "name": "Student 2", "course": "Course 2"},
    ]
    csv_bytes = create_byte_stream(data)
    result = csv_bytes_to_list(csv_bytes)
    assert result == data


def test_create_byte_stream_empty_data():
    csv_bytes = create_byte_stream([])
    assert csv_bytes == b""


def test_create_byte_stream_handles_quoted_fields():
    data = [
        {"student_id": "1234", "name": 'Student "One"', "course": "Course, A"},
        {"student_id": "5678", "name": 'Student "Two"', "course": "Course, B"},
    ]
    csv_bytes = create_byte_stream(data)
    result = csv_bytes_to_list(csv_bytes)
    assert result == data


def test_create_byte_stream_consistent_header_order():
    data = [
        {"student_id": "1234", "name": "Alice", "course": "Math"},
        {"student_id": "5678", "name": "Bob", "course": "Science"},
    ]
    csv_bytes = create_byte_stream(data)
    csv_string = csv_bytes.decode("utf-8")
    header_line = csv_string.splitlines()[0]
    expected_header = ",".join(data[0].keys())
    assert header_line == expected_header


def test_create_byte_stream_special_characters():
    data = [
        {"student_id": "1234", "name": "Student 1", "course": "Line1\nLine2"},
        {"student_id": "5678", "name": "Student 2", "course": "Value with, comma"},
    ]
    csv_bytes = create_byte_stream(data)
    result = csv_bytes_to_list(csv_bytes)
    assert result == data
