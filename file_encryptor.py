#!/bin/python

import src.hmacrypt as hmacrypt
import sys
import os

# Getting and requiring exactly 1 argument
if len(sys.argv) != 2:
    print("Usage: python3 file_encryptor.py <filepath>")
    sys.exit(1)
filepath = sys.argv[1]

# The file should exist and be readable
if not os.path.isfile(filepath):
    print("File not found")
    sys.exit(1)


# FIXME Do the below operations in chunks


# Read the file
with open(filepath, "rb") as f:
    filebytes = f.read()
encodedbytes = hmacrypt.self_encrypt(filebytes, encoded=True)

# Write the file
with open(filepath + ".enc", "wb") as f:
    f.write(encodedbytes)