#!/bin/python

import src.hmacrypt as hmacrypt
import sys
import os
import bysp

# Getting and requiring exactly 1 argument
if len(sys.argv) != 2:
    print("Usage: python3 file_encryptor.py <filepath>")
    sys.exit(1)
filepath = sys.argv[1]

# The file should exist and be readable
if not os.path.isfile(filepath):
    print("File not found")
    sys.exit(1) 

# Getting file size
size = os.path.getsize(filepath)
print("File size: " + str(size) + " bytes")
# REVIEW Dividing the file into  1MB chunks
chunks = size // 1048576
print("Chunks: " + str(chunks))
bysp.split_file(filepath, chunks)
exit(0)

hmacrypt.self_encrypt_file(filepath, filepath + ".enc")
print("Encrypted file: " + filepath + ".enc")