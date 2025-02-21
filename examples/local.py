from gdpr_obfuscator import Obfuscator

obfuscator = Obfuscator()

def main():
    return obfuscator.local(location="../mock_data.csv", pii_fields=["name", "email"])

if __name__ == "__main__":
    main()