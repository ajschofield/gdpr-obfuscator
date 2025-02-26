from gdpr_obfuscator import Obfuscator

obfuscator = Obfuscator()

json_input = (
    '{"file_path": "./test/data/mock_data.csv", "pii_fields": ["name", "email"]}'
)

print(obfuscator.process_local(json_input))
