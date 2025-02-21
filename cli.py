import argparse
from gdpr_obfuscator import Obfuscator

# This is a simple CLI for demonstration and doesn't undergo the same level
# of testing as the core library.


def main():
    parser = argparse.ArgumentParser(
        prog="GDPR-Obfuscator",
        description="Obfuscate sensitive data stored locally or in an AWS environment",
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
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

    if args.local and not args.s3:
        obfuscated_data = obfuscator.process_local(args.local, args.pii)
    else:
        obfuscated_data = obfuscator.process_s3(args.s3, args.pii)

    print(obfuscated_data)


if __name__ == "__main__":
    main()
