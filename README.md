# hmacrypt
encryption / decryption / signing / verifying using RSA and ECDSA a deterministic Key Derivation from password+hmac_secret by an hardware key.

## Requirements (BEFORE everything else) & Credits

Ensure to have the following library installed:

- https://github.com/dido/fido2-hmac-secret

This library is at the core of this repository, so all the credits are dued to the author.

### Requirements quickstart

    git clone https://github.com/dido/fido2-hmac-secret
    cd fido2-hmac-secret
    make release
    make all
    sudo make install

#### Dependencies errors

libfido2, libcbor and libsodium are needed for the above library to work properly.

On Ubuntu 23.10 (untested on other platforms and flavors):

    sudo apt install lifido2-dev
    sudo apt install libcbor-dev
    sudo apt install libsodium-dev

## FAQ

- A .keyfile without the passphrase AND the hardware key is not usable and won't be recoverable
- Remember to always "conda activate ./hmacenv" prior to running anything from here

## Features

- 2fa encryption/decryption using RSA deterministic Key Derivation
- 2fa signing/verifying using ECDSA deterministic Key Derivation
- Possibility to use the same or different keyfiles to enhance security
- Consequently, supports for a wide range of hardware keys as long as they are compatible with libfido2
- Low footprint: requires just two (or three) python library and a single system library
- Readable: you are free and encouraged to tinker with this library

## What is this
As hardware keys (namely FIDO2 keys) can expose hmac_secret as an extension, and being this secret paired to a passphrase to output a deterministic 128 byte secret, this secret can be used for on-the-fly RSA key derivation and consequent encryption/decryption using the RSA Keypair.

## Quickstart

- Ensure you have miniconda, anaconda or anyway conda
- Execute the install.sh script
- You can either activate the environment (optionally) or just run the binaries that are configured to use the newly created environment
- Enjoy

## Manual start (even outside conda if you have Python <= 3.10)

- Install requirements.txt
- Enjoy

## First run

Once enrolled with the install.sh script or by manually executing src/bin/first_run, you will have a password-protected .keyfile in the bins directory.

That .keyfile will be used by the various scripts.

## Documentation and Examples

The present repository contains various easy to use examples in the examples folder.
Once you have finished setting up your environment (either with the install.sh script or with conda or manually), you can grasp a quick view of this library by executing the examples below.

The examples provided allows everybody to use this library programmatically.

### Standalone tools

You can also use the standalone tools in the root folder to encrypt / decrypt files and strings.

The tools allows you to sign and verify strings.

Please note that the tools are just an utility and may not be suited for large data inputs.

### Documentation

This is the documentation for hmacrypt.py library (you can find it in src).

#### How to use this library

Ideally, you should just obtain a copy of the src directory.
Please do not change the directory's name as it is used in the various imports.
If you (as expected) need to change the directory's name, please create a parent directory with the desired name and move the src directory to the newly created directory.

As per the various examples, you can then import the library with:

    import src.hmacrypt as hmacrypt

Or the path you used for the library.

*If you REALLY have to change the src directory name, please correct the various paths inside.*


#### inferECDSAKeys

Definition:

    def inferECDSAKeys(hidePrivate=False, savePublic=False, keyfilePath="src/bins/.keyfile")

Parameters:

- hidePrivate (boolean, default to False); if True, does not return the private key
- savePublic (boolean, default to False); if True, saves the public key to a file
- keyfilePath (string, default to the bins path); allows the usage of different keyfiles, for example to use a different hmac_secret

#### inferRSAKeys

Definition:

    def inferRSAKeys(hidePrivate=False, savePublic=False, keyfilePath="src/bins/.keyfile")

Parameters:

- hidePrivate (boolean, default to False); if True, does not return the private key
- savePublic (boolean, default to False); if True, saves the PEM encoded public key to a file
- keyfilePath (string, default to the bins path); allows the usage of different keyfiles, for example to use a different hmac_secret

#### self_sign

Definition:

    def self_sign(message):

Parameters:

- message (string); the message to sign

#### self_verify

Definition:

    def self_verify(signature, message):

Parameters:

- signature (bytes); the signature to verify
- message (string); the message that is supposed to be corresponding to the signature

#### self_encrypt

Definition:

    def self_encrypt(secret, encoded=False):

Parameters:

- secret (string or bytes); the secret to encrypt
- encoded (boolean, default to False); if True, avoid encoding the secret as it expects bytes

#### self_decrypt

Definition:

    def self_decrypt(encrypted):

Parameters:

- encrypted (bytes); the encrypted secret in bytes as outputted by self_encrypt

#### self_encrypt_file

*N.B. The method does not include any optimization for large files. Please do not use this method for large files without a proper logic being used. Prefer encoding in chunks in that case, by using self_encrypt and self_decrypt properly.*

Definition:

    def self_encrypt_file(filepath, outpath):

Parameters:

- filepath (string); the path to the file to be encrypted
- outpath (string); the path to the encrypted file to be saved

#### self_decrypt_file

*N.B. The method does not include any optimization for large files. Please do not use this method for large files without a proper logic being used. Prefer encoding in chunks in that case, by using self_encrypt and self_decrypt properly.*

Definition:

    def self_decrypt_file(filepath, outpath):

Parameters:

- filepath (string); the path to the file to be decrypted
- outpath (string); the path to the decrypted file to be saved


### Examples

#### string_encryption_example.py

The script encodes and encrypt a string using the same inferred RSA keypair as above and then decrypts it.

#### file_encryption_example.py

The script creates, encodes and encrypts a simple text file, then decrypts it using the same keypair as above.

#### string_sign_and_verify.py

The script sign and verify a given string using the keypair derived from the hmac_secret + password + key

## Known Issues

- Python 3.11 breaks things in building pycrypto, that's why the prepared env is Python 3.10

## Disclaimer

This is just an experiment. While it should be safe, please review every step involved before using this in production. 

Also note that your encryption is as secure as your passphrase and your habits.

Last but not least: don't ever lose your hardware key.

## Credits

I used and modified https://pypi.org/project/deterministic-rsa-keygen/ to fit the requirements of this project.