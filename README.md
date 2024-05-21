# AppVet

**AppVet** is a cli tool to statically vet mobile applications.

## Installation

```
python3 -m pip install -r requirements.txt
```


## Usage

```
usage: analyze.py [-h] [-i] [-a] [-p] [-q] ipa_file

Extract values from an IPA file's Info.plist

positional arguments:
  ipa_file           Path to the IPA file

options:
  -h, --help         show this help message and exit
  -i, --info         Print application information
  -a, --ats          Print ATS settings
  -p, --permissions  Print permissions
  -q, --quiet        Do not print header
```
