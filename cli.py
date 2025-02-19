import argparse
from obfuscator.read import DataReader
from obfuscator.obfuscate import obfuscate
from obfuscator.logger import get_logger
from obfuscator.csv_writer import create_byte_stream


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

    log_level = "DEBUG" if args.verbose else "INFO"
    logger = get_logger("CLI", log_level)

    reader = DataReader(log_level)

    if args.local and not args.s3:
        logger.debug("Read data from local path")
        data = reader.read_local(args.local)
    else:
        logger.debug("Read data from S3")
        data = reader.read_s3(args.s3)

    obfuscated_data = obfuscate(data, args.pii)

    return create_byte_stream(obfuscated_data)


if __name__ == "__main__":
    main()
