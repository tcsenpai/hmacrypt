import subprocess
from src.libs.seedable_rsa import decrypt, encrypt, generate_rsa_key
from src.libs.seedable_ecdsa import generate_ecdsa_key, sign, verify
from src.libs.seedable_aes import self_encrypt_aes, self_decrypt_aes

# INFO This method derives the HMAC secret from the hardware key and the stored secret
def getHMACSecret(keyfilePath="src/bins/.keyfile"):
    """Infer keys from the secret stored in the hardware key"""
    hmac_secret_raw = subprocess.check_output(
        ["src/bins/hmac_secret_regenerate", keyfilePath]
    )
    # Convert to string
    hmac_secret_dirty = hmac_secret_raw.decode("utf-8")
    # Divide lines and keep last one
    hmac_secret = hmac_secret_dirty.splitlines()[-1]
    hmac_secret = hmac_secret.strip()
    return hmac_secret

# INFO The following methods are proxies to the AES methods
# NOTE The AES methods generate a cipher on the fly based on the getHMACSecret method

def encrypt_aes(message):
    seed = getHMACSecret()
    return self_encrypt_aes(seed, message)

def decrypt_aes(encrypted):
    seed = getHMACSecret()
    return self_decrypt_aes(seed, encrypted)

# INFO This method derives an ECDSA keypair from the stored secret and the hardware key
def inferECDSAKeys(hidePrivate=False, savePublic=False):
    hmac_secret = getHMACSecret()
    key_pair = generate_ecdsa_key(hmac_secret)
    # We use them in memory, we never save them
    # Privacy should be possible here
    if hidePrivate:
        private_key = "REDACTED"
    else:
        private_key = key_pair[0]
    public_key = key_pair[1]
    # Saving public key is permitted
    if savePublic:
        with open("public_ecdsa_key.pem", "wb+") as f:
            f.write(public_key.to_pem())
    return private_key, public_key

def self_sign(message):
    """Sign a message with the private key"""
    private_key, public_key = inferECDSAKeys()
    signature = sign(private_key, message)
    return signature

def self_verify(signature, message):
    """Verify a message with the public key"""
    private_key, public_key = inferECDSAKeys(hidePrivate=True)
    return verify(public_key, signature, message)

# INFO This method derives a RSA keypair from the stored secret and the hardware key
def inferRSAKeys(hidePrivate=False, savePublic=False):
    hmac_secret = getHMACSecret()
    secret_key = generate_rsa_key(hmac_secret)  # RSA Key (2048) derivation
    # We use them in memory, we never save them
    # Privacy should be possible here
    if hidePrivate:
        private_key = "REDACTED"
    else:
        private_key = secret_key.exportKey("PEM")
    public_key = secret_key.publickey().exportKey("PEM")
    # Saving public key is permitted
    if savePublic:
        with open("public_rsa_key.pem", "wb") as f:
            f.write(public_key)
    return private_key, public_key


# NOTE All the below methods generates keys on the fly to avoid persistance
# NOTE You should NEVER save the keypair to disk or even to a globlal variable
# NOTE Security is only guaranteed by the observance of the above rule

# STRINGS


def self_encrypt(secret, encoded=False):
    """Encrypt secret with public key"""
    private_key, public_key = inferRSAKeys(hidePrivate=True)
    secret = encrypt(secret, public_key, encoded)
    return secret


def self_decrypt(encrypted):
    """Decrypt secret with private key"""
    private_key, public_key = inferRSAKeys()
    secret = decrypt(encrypted, private_key)
    return secret


# SMALL FILES


def self_encrypt_file(filepath, outpath):
    """Encrypt file with public key"""
    private_key, public_key = inferRSAKeys(hidePrivate=True)
    with open(filepath, "rb") as f:
        filebytes = f.read()
    encrypted = encrypt(filebytes, public_key, encoded=True)
    with open(outpath, "wb") as f:
        f.write(encrypted)
    return outpath


def self_decrypt_file(filepath, outpath):
    """Decrypt file with private key"""
    private_key, public_key = inferRSAKeys()
    with open(filepath, "rb") as f:
        filebytes = f.read()
    decrypted = decrypt(filebytes, private_key)
    with open(outpath, "wb") as f:
        f.write(decrypted)
    return outpath


# TODO LARGE FILES
