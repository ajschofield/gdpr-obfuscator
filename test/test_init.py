from obfuscator.__init__ import main


def test_main_integration():
    test_source = "s3://test-bucket/data.csv"
    result = main(test_source, ["name"], log_level="DEBUG")
    result_str = result.decode("utf-8")
    assert "John" not in result_str
    assert "***" in result_str
