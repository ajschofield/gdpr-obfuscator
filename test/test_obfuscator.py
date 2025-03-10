from gdpr_obfuscator.obfuscate import obfuscate_data
import pytest


def test_obfuscate_data_with_valid_pii_fields():
    data = [
        {
            "student_id": "1234",
            "name": "John Smith",
            "course": "Software",
            "email_address": "j.smith@email.com",
        },
        {
            "student_id": "5678",
            "name": "Jane Doe",
            "course": "Data Science",
            "email_address": "j.doe@email.com",
        },
    ]
    pii_fields = ["name", "email_address"]
    expected = [
        {
            "student_id": "1234",
            "name": "***",
            "course": "Software",
            "email_address": "***",
        },
        {
            "student_id": "5678",
            "name": "***",
            "course": "Data Science",
            "email_address": "***",
        },
    ]

    result = obfuscate_data(data, pii_fields)
    assert result == expected


def test_obfuscate_data_with_missing_pii_field():
    data = [
        {"student_id": "1234", "name": "John Smith", "course": "Software"},
        {
            "student_id": "5678",
            "name": "Jane Doe",
            "course": "Data Science",
            "email_address": "j.doe@email.com",
        },
    ]
    pii_fields = ["name", "email_address"]

    with pytest.raises(Exception):
        obfuscate_data(data, pii_fields)


def test_obfuscate_data_with_no_data():
    data = []
    pii_fields = ["name", "email_address"]
    expected = []

    result = obfuscate_data(data, pii_fields)
    assert result == expected


def test_obfuscate_data_with_empty_pii_fields():
    data = [
        {
            "student_id": "1234",
            "name": "John Smith",
            "course": "Software",
            "email_address": "j.smith@email.com",
        }
    ]
    pii_fields = []
    expected = data.copy()

    result = obfuscate_data(data, pii_fields)
    assert result == expected
