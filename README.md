# GDPR Obfuscator - Launchpad Project

1. [Overview](#overview)
2. [Minimum Viable Product (MVP)](#minimum-viable-product-mvp)
3. [Setup](#setup)
4. [Usage](#usage)

## Overview

A Python library designed to detect and remove Personally Identifiable Information (PII) from data formats such as CSV, JSON and Parquet formats.

## Minimum Viable Product (MVP)

The MVP covers:
1. Reading a JSON string containing the S3 location of the CSV file and the names of the fields that are required to be obfuscated
2. Ingesting the CSV file containing data records (with a primary key) from an AWS S3 bucket
3. Obfuscating chosen PII fields (e.g. `name`, `email_address`) by replacing their values with an obfuscated string (`***`)
4. Producing an output CSV file (or a byte-stream) that maintains the original structure but with sensitive fields changed

This meets the requirements under the General Data Protection Regulation [(GDPR)](https://ico.org.uk/media/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr-1-1.pdf) to ensure that all data containing information that can be used to identify an individual should be anonymised.

## Setup

## Usage
