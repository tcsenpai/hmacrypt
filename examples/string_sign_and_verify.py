#!./hmacenv/bin/python

import src.hmacrypt as hmacrypt
import sys
import os

# Getting and requiring exactly 1 argument
if len(sys.argv) != 2:
    print("Usage: python3 string_decryptor.py <binary_file_with_encrypted_string>")
    sys.exit(1)
stringToSign = sys.argv[1].encode()


signed = hmacrypt.self_sign(stringToSign)

with open("signed.txt", "wb+") as signedFile:
    signedFile.write(signed)

print(signed)

# Verify
with open("signed.txt", "rb") as f:
    signed = f.read()
verified = hmacrypt.self_verify(signed, stringToSign)
print(verified)
