import argparse
import json
from gdpr_obfuscator import Obfuscator

# This is a simple CLI for demonstration and doesn't undergo the same level
# of testing as the core library.


def main():
    parser = argparse.ArgumentParser(
        prog="GDPR-Obfuscator",
        description="Obfuscate sensitive data stored locally or in an AWS environment",
    )

    loc = parser.add_mutually_exclusive_group(required=True)
    loc.add_argument("-l", "--local", help="Local path to file")
    loc.add_argument("-s", "--s3", help="URI path to file stored in S3")

    parser.add_argument(
        "-p",
        "--pii",
        nargs="+",
        required=True,
        help="List of PII fields to obfuscate, separated by spaces",
    )

    args = parser.parse_args()

    obfuscator = Obfuscator()

    json_input = json.dumps(
        {
            "file_path": args.local if args.local else args.s3,
            "pii_fields": args.pii,
        }
    )

    if args.local and not args.s3:
        obfuscated_data = obfuscator.process_local(json_input)
    else:
        obfuscated_data = obfuscator.process_s3(json_input)

    print(obfuscated_data)


if __name__ == "__main__":
    main()
