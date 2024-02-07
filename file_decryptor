#!/bin/python

import src.hmacrypt as hmacrypt
import sys
import os

# Getting and requiring exactly 1 argument
if len(sys.argv) != 2:
    print("Usage: python3 file_decryptor.py <filepath>")
    sys.exit(1)
filepath = sys.argv[1]

# The file should exist and be readable
if not os.path.isfile(filepath):
    print("File not found")
    sys.exit(1)

hmacrypt.self_decrypt_file(filepath, filepath + ".enc")
print("decrypted file: " + filepath + ".enc")