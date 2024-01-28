import src.hmacrypt as hmacrypt


encrypted = hmacrypt.self_encrypt("My secret")
print(encrypted)

decrypted = hmacrypt.self_decrypt(encrypted)
print(decrypted)
