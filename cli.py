import argparse
from obfuscator.csv_reader import read

def main():
    parser = argparse.ArgumentParser(description="gdpr-obfuscator")
    # Require user to either choose a local file or an S3 object
    loc = parser.add_mutually_exclusive_group(required=True)
    loc.add_argument("--local")
    loc.add_argument("--s3")
    args = parser.parse_args()

    if args.local and not args.s3:
        print(read(args.local))
    else:
        pass

if __name__ == "__main__":
    main()
