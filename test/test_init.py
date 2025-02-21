from gdpr_obfuscator import Obfuscator
import moto

obfuscator = Obfuscator()


def test_main_integration():
    test_source = "s3://test-bucket/data.csv"
    result = obfuscator.process_s3(test_source, ["name"])
    result_str = result.decode("utf-8")
    assert "John" not in result_str
    assert "***" in result_str
