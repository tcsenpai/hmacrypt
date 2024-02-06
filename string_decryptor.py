import src.hmacrypt as hmacrypt
import sys
import os

# Getting and requiring exactly 1 argument
if len(sys.argv) != 2:
    print("Usage: python3 string_decryptor.py <binary_file_with_encrypted_string>")
    sys.exit(1)
filepath = sys.argv[1]

# The file should exist and be readable
if not os.path.isfile(filepath):
    print("File not found")
    sys.exit(1)

with open(filepath, "rb") as f:
    stringToDecrypt = f.read()
decrypted = hmacrypt.self_decrypt(stringToDecrypt)

with open("decrypted.txt", "wb+") as decryptedFile:
    decryptedFile.write(decrypted)
print(decrypted)
