# csv_reader.py - tests
# Author: Alex Schofield

from main import csv_reader
import pytest

def test_empty_csv_should_return_no_content():
    content = ""
    result = csv_reader(content)
    expected = []
    assert result == expected

def test_csv_with_header_only_should_return_no_content():
    content = "student_id,name,course\n"
    result = csv_reader(content)
    expected = []
    assert result == expected

def test_csv_with_valid_data():
    content = (
        "student_id,name,course\n"
        "1234,Student 1,Course 1\n"
        "5678,Student 2,Course 2\n"
        )
    result = csv_reader(content)
    expected = [
        {"student_id": "1234", "name": "Student 1", "course": "Course 1"},
        {"student_id": "5678", "name": "Student 2", "course": "Course 2"},
        ]
    assert result == expected 

def test_csv_with_quoted_fields_should_be_sanitised():
    content = (
        'student_id,name,course\n'
        '1234,"Student 1","Course 1"\n'
        '5678,"Student 2","Course 2"\n'
    )
    result = csv_reader(content)
    expected = [
        {"student_id": "1234", "name": "Student 1", "course": "Course 1"},
        {"student_id": "5678", "name": "Student 2", "course": "Course 2"},
    ]
    assert result == expected

@pytest.mark.skip(reason="Not implemented yet")
def test_non_csv_file_should_return_no_content():
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_csv_file_with_embedded_newline_should_be_sanitised():
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_csv_file_with_embedded_comma_should_be_sanitised():
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_csv_file_with_embedded_quote_should_be_sanitised():
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_csv_file_with_null_values_should_be_transformed_to_empty_string():
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_csv_file_with_non_string_data_should_be_transformed_to_empty_string():
    pass

