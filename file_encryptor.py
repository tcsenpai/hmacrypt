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

hmacrypt.self_encrypt_file(filepath, filepath + ".enc")
print("Encrypted file: " + filepath + ".enc")
hmacrypt.self_decrypt_file(filepath + ".enc", filepath + ".dec.png")
print("Decrypted file: " + filepath + ".dec.png")