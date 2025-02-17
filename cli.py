import argparse
from obfuscator.csv_reader import CSVReader
from obfuscator.obfuscate import obfuscate
from obfuscator.logger import get_logger

logger = get_logger("CLI")


def main():
    parser = argparse.ArgumentParser(description="gdpr-obfuscator")
    # Require user to either choose a local file or an S3 object
    loc = parser.add_mutually_exclusive_group(required=True)
    loc.add_argument("--local")
    loc.add_argument("--s3")

    parser.add_argument("--pii", nargs="+", required=True)
    
    args = parser.parse_args()

    if args.local and not args.s3:
        logger.debug("User chose to read CSV from local path")
        reader = CSVReader()
        data = reader.read_local(args.local)
        print(data)
    else:
        logger.debug("User chose to read CSV from S3")


if __name__ == "__main__":
    main()
