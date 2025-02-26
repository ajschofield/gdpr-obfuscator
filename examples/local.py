from gdpr_obfuscator import Obfuscator

obfuscator = Obfuscator()

json_input = '{"file_path": "./test/data/large_dataset.csv", "pii_fields": ["full_name", "email_address"]}'

print(obfuscator.process_local(json_input))
