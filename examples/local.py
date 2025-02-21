from gdpr_obfuscator import Obfuscator

obfuscator = Obfuscator()


def main():
    print(obfuscator.process_local(path="mock_data.csv", pii_fields=["name", "email"]))


if __name__ == "__main__":
    main()
