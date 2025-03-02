# GDPR Obfuscator - Launchpad Project

1. [Overview](#overview)
2. [Minimum Viable Product (MVP)](#minimum-viable-product-mvp)
    1. [Additional Features](#additional-features)
4. [Setup](#setup)
    1. [Prerequisites](#prerequisites)
    2. [Installation](#installation)
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

1. Clone the repository:

```bash
git clone --recurse-submodules https://github.com/ajschofield/gdpr-obfuscator.git
cd gdpr-obfuscator
```

2. Install dependencies using poetry

```bash
# Production
poetry install
# Developer (optional)
poetry install --dev
```

## Usage
