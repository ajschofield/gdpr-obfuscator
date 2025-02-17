from obfuscator.obfuscate import obfuscate

# Check if the function does what its supposed to and can obfuscate 
# valid PII fields in a list of dictionaries
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

    result = obfuscate(data, pii_fields)
    assert result == expected

# Check if the function can obfuscate data even when some PII
# fields are missing from some of the data, returning a list of dictionaries
# but with the missing PII fields obfuscated and the rest of the data intact
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
    expected = [
        {"student_id": "1234", "name": "***", "course": "Software"},
        {
            "student_id": "5678",
            "name": "***",
            "course": "Data Science",
            "email_address": "***",
        },
    ]

    result = obfuscate(data, pii_fields)
    assert result == expected

# Check if the function can handle an empty list of data, returning an empty list
def test_obfuscate_data_with_no_data():
    data = []
    pii_fields = ["name", "email_address"]
    expected = []

    result = obfuscate(data, pii_fields)
    assert result == expected

# Check if the function can handle an empty list of PII fields, returning the data as is
# without mutating it
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

    result = obfuscate(data, pii_fields)
    assert result == expected
