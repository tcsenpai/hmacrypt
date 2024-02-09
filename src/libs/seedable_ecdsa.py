import ecdsa
from hashlib import sha256

# Sign
def sign(sk, message):
    """Sign a message using a private key"""
    # Sign a message using a private key
    signature = sk.sign(message, hashfunc=sha256)
    return signature

# Verify
def verify(vk, signature, message):
    """Verify a message using a public key"""
    # Verify a message using a public key
    return vk.verify(signature, message, hashfunc=sha256)

# Generate a key pair using a seed
def generate_ecdsa_key(seed):
    """Generate a key pair using a seed"""
    seed = seed.encode()
    hashed = sha256(seed).digest()
    # Generate a key pair using a seed
    sk = ecdsa.SigningKey.from_string(hashed, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    return sk, vk

