from gdpr_obfuscator import Obfuscator

obfuscator = Obfuscator()


print(obfuscator.process_local(path="mock_data.csv", pii_fields=["name", "email"]))
