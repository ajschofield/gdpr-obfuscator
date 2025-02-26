import json
import pytest
from unittest.mock import patch
from cli import main


@pytest.fixture
def mock_obfuscator():
    with patch("cli.Obfuscator") as MockObfuscator:
        mock_instance = MockObfuscator.return_value
        mock_instance.process_local.return_value = (
            '{"status": "success", "data": "local_obfuscated_data"}'
        )
        mock_instance.process_s3.return_value = (
            '{"status": "success", "data": "s3_obfuscated_data"}'
        )
        yield mock_instance


def test_local_obfuscation_successfully_runs(mock_obfuscator):
    test_args = [
        "GDPR-Obfuscator",
        "--local",
        "test_local_file.json",
        "--pii",
        "name",
        "email",
    ]
    with patch("sys.argv", test_args):
        with patch("builtins.print") as mock_print:
            main()
            expected_payload = json.dumps(
                {"file_path": "test_local_file.json", "pii_fields": ["name", "email"]}
            )
            mock_obfuscator.process_local.assert_called_once_with(expected_payload)
            mock_print.assert_called_once_with(
                '{"status": "success", "data": "local_obfuscated_data"}'
            )


def test_s3_obfuscation_successfully_runs(mock_obfuscator):
    test_args = [
        "GDPR-Obfuscator",
        "--s3",
        "s3://bucket/test_file.json",
        "--pii",
        "name",
        "email",
    ]
    with patch("sys.argv", test_args):
        with patch("builtins.print") as mock_print:
            main()
            expected_payload = json.dumps(
                {
                    "file_path": "s3://bucket/test_file.json",
                    "pii_fields": ["name", "email"],
                }
            )
            mock_obfuscator.process_s3.assert_called_once_with(expected_payload)
            mock_print.assert_called_once_with(
                '{"status": "success", "data": "s3_obfuscated_data"}'
            )


def test_execution_fails_with_missing_required_arguments():
    test_args = ["GDPR-Obfuscator"]
    with patch("sys.argv", test_args):
        with pytest.raises(SystemExit):
            main()


def test_execution_fails_with_missing_pii_argument():
    test_args = ["GDPR-Obfuscator", "--local", "test_local_file.json"]
    with patch("sys.argv", test_args):
        with pytest.raises(SystemExit):
            main()


def test_execution_fails_with_both_local_and_s3_arguments_present():
    test_args = [
        "GDPR-Obfuscator",
        "--local",
        "test_local_file.json",
        "--s3",
        "s3://bucket/test_file.json",
        "--pii",
        "name",
    ]
    with patch("sys.argv", test_args):
        with pytest.raises(SystemExit):
            main()
