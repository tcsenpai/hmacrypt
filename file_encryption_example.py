import src.hmacrypt as hmacrypt

with open("test", "w+") as f:
    f.write("secret message")

encrypted = hmacrypt.self_encrypt_file("test", "test_encrypted")
print(encrypted)

decrypted = hmacrypt.self_decrypt_file("test_encrypted", "test_decrypted")
print(decrypted)
