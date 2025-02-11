# csv_reader.py - tests
# Author: Alex Schofield

from csv_reader import csv_reader

def test_empty_csv_should_return_no_content():
    pass

def test_csv_with_header_only_should_return_no_content():
    pass

def test_csv_with_valid_data_should_return_obfuscated_content():
    pass

def test_csv_with_quoted_fields_should_be_sanitised():
    pass

def test_non_csv_file_should_return_no_content():
    pass

def test_csv_file_with_embedded_newline_should_be_sanitised():
    pass

def test_csv_file_with_embedded_comma_should_be_sanitised():
    pass

def test_csv_file_with_embedded_quote_should_be_sanitised():
    pass

def test_csv_file_with_null_values_should_be_transformed_to_empty_string():
    pass

def test_csv_file_with_non_string_data_should_be_transformed_to_empty_string():
    pass

