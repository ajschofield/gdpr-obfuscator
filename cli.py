import argparse
from obfuscator import csv_reader

def main():
    parser = argparse.ArgumentParser(description="gdpr-obfuscator")
    parser.add_argument("--local", help="Path to local CSV file")
    parser.add_argument("--s3", help="Path to S3 object for CSV file")
    args = parser.parse_args()

if __name__ == "__main__":
    main()
