import subprocess

from src.libs.seedable_rsa import decrypt, encrypt, generate_key


# INFO This method is the core of the whole process as it derives a RSA keypair from the stored secret and the hardware key
def inferKeys(hidePrivate=False, savePublic=False, keyfilePath="src/bins/.keyfile"):
    """Infer keys from the secret stored in the hardware key"""
    hmac_secret_raw = subprocess.check_output(
        ["src/bins/hmac_secret_regenerate", keyfilePath]
    )
    # Convert to string
    hmac_secret_dirty = hmac_secret_raw.decode("utf-8")
    # Divide lines and keep last one
    hmac_secret = hmac_secret_dirty.splitlines()[-1]
    hmac_secret = hmac_secret.strip()
    secret_key = generate_key(hmac_secret)  # RSA Key (2048) derivation
    # We use them in memory, we never save them
    # Privacy should be possible here
    if hidePrivate:
        private_key = "REDACTED"
    else:
        private_key = secret_key.exportKey("PEM")
    public_key = secret_key.publickey().exportKey("PEM")
    # Saving public key is permitted
    if savePublic:
        with open("public_key.pem", "wb") as f:
            f.write(public_key)
    return private_key, public_key


# NOTE All the below methods generates keys on the fly to avoid persistance
# NOTE You should NEVER save the keypair to disk or even to a globlal variable
# NOTE Security is only guaranteed by the observance of the above rule

# STRINGS


def self_encrypt(secret, encoded=False):
    """Encrypt secret with public key"""
    private_key, public_key = inferKeys()
    secret = encrypt(secret, public_key, encoded)
    return secret


def self_decrypt(encrypted):
    """Decrypt secret with private key"""
    private_key, public_key = inferKeys()
    secret = decrypt(encrypted, private_key)
    return secret


# SMALL FILES


def self_encrypt_file(filepath, outpath):
    """Encrypt file with public key"""
    private_key, public_key = inferKeys(hidePrivate=True)
    with open(filepath, "rb") as f:
        filebytes = f.read()
    encrypted = encrypt(filebytes, public_key, encoded=True)
    with open(outpath, "wb") as f:
        f.write(encrypted)
    return outpath


def self_decrypt_file(filepath, outpath):
    """Decrypt file with private key"""
    private_key, public_key = inferKeys()
    with open(filepath, "rb") as f:
        filebytes = f.read()
    decrypted = decrypt(filebytes, private_key)
    with open(outpath, "wb") as f:
        f.write(decrypted)
    return outpath


# TODO LARGE FILES


# Self testing
if __name__ == "__main__":
    private_key, public_key = inferKeys()
    secret = encrypt("secret message", public_key)
    print(secret)
    decrypted = decrypt(secret, private_key)
    print(decrypted)
