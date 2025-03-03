# GDPR Obfuscator - Launchpad Project

1. [Overview](#overview)
2. [Minimum Viable Product (MVP)](#minimum-viable-product-mvp)
    1. [Additional Features](#additional-features)
4. [Setup](#setup)
    1. [Prerequisites](#prerequisites)
    2. [Installation](#installation)
        1. [Source](#from-source)
        2. [Prebuilt Package](#from-pypi)
5. [Usage](#usage)

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
