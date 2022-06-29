# ndcparser
A lightweight python package for standardizing and parsing National Drug Code (NDC) strings. 

NDCs are unique, numerical product identifiers for human drugs in the US and play an essential role in medical claims and billing, pharmaceutical commerce and distribution, and clinical support software. However, the format in which they are presented varies by their configurations (e.g. 5-4-2), use of delimiters (hyphens), and zero-padding. This creates a challenge for joining datasets that use the NDC as a primary key. Additionally, when NDCs are exported to CSV format, data loss can become an issue when the non-arbitrary leading zeros are stripped from the NDC. The ndcparser is a tool designed to address these problems by providing a means to standardize NDC strings to a uniform representation, that is the HIPAA standard 11 digit ndc format.  

### NDC Formats and Examples
* 5-4-2 format: 00999-0999-09
* 4-4-2 format: 0999-0999-09
* 5-4-1 format: 00999-0999-9
* 5-3-2 format: 00999-999-99

Unhyphenated formats also exist including the HIPAA standard format which is 11-digits, zero-padded, and unhyphenated (e.g., 00111222233).

## Features
- Convert NDC strings from various formats to the HIPAA standard 11-digit NDC format
- Parse segments from NDC strings (labeler code, product code, package code)
- Return an NDC in different formats

## Usage
1. Install `ndcparser` with pip, a tool for installing and managing python packages.
2. Parsing and formatting
```

```