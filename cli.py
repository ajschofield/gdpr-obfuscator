import argparse
import json
from obfuscator.csv_reader import CSVReader
from obfuscator.obfuscate import obfuscate
from obfuscator.logger import get_logger
from obfuscator.csv_writer import create_byte_stream

# Create the logger
logger = get_logger("CLI")


def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(
        prog="GDPR-Obfuscator",
        description="Obfuscate sensitive data stored locally or in an AWS environment",
    )
    # Require user to either choose a local file or an S3 object
    # The user can only choose one of these options or the program will exit
    # If not provided, the program will exit
    loc = parser.add_mutually_exclusive_group(required=True)
    loc.add_argument("-l", "--local")
    loc.add_argument("-s", "--s3")

    # Require user to provide a list of PII fields to obfuscate
    # e.g. --pii name email_address
    # If not provided, the program will exit
    parser.add_argument("-p", "--pii", nargs="+", required=True)

    # Parse the arguments
    args = parser.parse_args()

    # Create the CSVReader object
    reader = CSVReader()

    # Read the CSV data based on the user's choice of local or S3
    if args.local and not args.s3:
        logger.debug("User chose to read CSV from local path")
        data = reader.read_local(args.local)
        # For debug purposes, log the data read from the CSV
        logger.debug("Contents: " + str(data))
    else:
        logger.debug("User chose to read CSV from S3")
        data = reader.read_s3(args.s3)
        logger.debug("Contents: " + str(data))

    # Obfuscate the data based on the user's choice of PII fields
    obfuscated_data = obfuscate(data, args.pii)
    # For debug purposes, log the obfuscated data as JSON for readability
    logger.debug("Obfuscated data (JSON): " + json.dumps(obfuscated_data, indent=4))
    return create_byte_stream(obfuscated_data)


# If the script is run directly (as it should be), call the main function
if __name__ == "__main__":
    main()
