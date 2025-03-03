# GDPR Obfuscator - Launchpad Project

## Overview

A Python library designed to detect and remove Personally Identifiable Information (PII) from CSV files stored in an AWS S3 bucket.

## Minimum Viable Product (MVP)

The MVP covers:
1. Reading a JSON string containing the S3 location of the CSV file and the names of the fields that are required to be obfuscated
2. Ingesting the CSV file containing data records (with a primary key) from an AWS S3 bucket
3. Obfuscating chosen PII fields (e.g. `name`, `email_address`) by replacing their values with an obfuscated string (`***`)
4. Returning the obfuscated data as a byte-stream that maintains the original structure but with sensitive fields changed

This meets the requirements under the General Data Protection Regulation [(GDPR)](https://ico.org.uk/media/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr-1-1.pdf) to ensure that all data containing information that can be used to identify an individual should be anonymised.

## Setup

### Prerequisites

- Python >= 3.13
- Poetry >= 2.0.1

### Installation

There are two ways to install the package:

#### Source

```bash
git clone https://github.com/ajschofield/gdpr-obfuscator.git
cd gdpr-obfuscator
poetry install
```

#### Prebuilt Package

Download the latest release from [here](https://github.com/ajschofield/gdpr-obfuscator/releases/latest) and install using `pip`:

```bash
# Package name may be different to what is below
pip install gdpr_obfuscator-0.1.0-py3-none-any.whl
```

## Usage

The `Obfuscator` class can be imported directly into your Python code. Once instiantiated, you may call either the `process_s3` or `process_local` method. Each method takes a JSON string as the input, which must contain `file_path` and `pii_fields`.

```json
{
    "file_path": "s3://bucket-name/file-name.csv",
    "pii_fields": ["name", "email_address"]
}
```

Both methods return a byte-stream containing the obfuscated data which can be used with the put_object method in the boto3 library to upload the data reliably back to S3.

```python
from gdpr_obfuscator import Obfuscator
import json

input = json.dumps({
    "file_path": "s3://bucket-name/file-name.csv",
    "pii_fields": ["name", "email_address"]
})

obfuscator = Obfuscator()
result = obfuscator.process_s3(input)

print(result.decode("utf-8"))
```

Alternatively, there is a command line interface available to use the package from the terminal. The CLI is not packaged with the library, so you will have to follow the steps in the [source installation](#source) section to use it.

```bash
❯❯ poetry run python cli.py --help
usage: GDPR-Obfuscator [-h] (-l LOCAL | -s S3) -p PII [PII ...]

Obfuscate sensitive data stored locally or in an AWS environment

options:
  -h, --help            show this help message and exit
  -l, --local LOCAL     Local path to file
  -s, --s3 S3           URI path to file stored in S3
  -p, --pii PII [PII ...]
                        List of PII fields to obfuscate, separated by spaces
```

```bash
❯❯ poetry run python cli.py -l test/data/mock_data.csv -p name
student_id,name,course,cohort,graduation_date,email_address
1,***,UX/UI Design Bootcamp,2/29/2024,7/11/2024,jleger0@facebook.com
2,***,Digital Marketing Bootcamp,2/24/2024,9/6/2024,cadrian1@gizmodo.com
3,***,UX/UI Design Bootcamp,3/13/2024,10/24/2024,whugnin2@archive.org
4,***,Artificial Intelligence Bootcamp,2/24/2024,9/14/2024,aspight3@4shared.com
5,***,Artificial Intelligence Bootcamp,1/31/2024,9/4/2024,dcowpland4@dot.gov
6,***,Digital Marketing Bootcamp,2/8/2024,,gkliement5@auda.org.au
7,***,Internet of Things Bootcamp,2/21/2024,7/16/2024,
8,***,Mobile App Development Bootcamp,2/17/2024,7/15/2024,smyrkus7@i2i.jp
9,***,Game Development Bootcamp,3/1/2024,9/7/2024,nryal8@symantec.com
...
```