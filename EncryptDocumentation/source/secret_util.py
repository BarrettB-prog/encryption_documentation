"""Contains functions for handling encrypted secrets.

Includes functionality to check for an encrypted file containing
a secret in the user's home directory, decrypt it if it exists, or
prompt the user to enter a new secret which will then be encrypted
and saved for future use.

"""

"""Standard and Third Party imports"""
from cryptography.fernet import Fernet
import pathlib
import getpass
import argparse



def get_enc_secret(file_name):
    """Retrieves the encrypted secret from a file in the user's home directory.

    If the file exists, the function reads the encrypted key and secret,
    decrypts the secret, and returns it. If the file does not exist,
    it prompts the user to enter a secret, encrypts it, and saves it to the file.
    """
    file_path = pathlib.Path.home() / (file_name + ".enc")
    if file_path.exists():
        with open(file_path, "r") as enc_file:
            for line in enc_file:
                enc_line = line
        enc_token = enc_line.split(",")
        key = bytes(enc_token[0], "utf-8")
        encrypted_token = bytes(enc_token[1], "utf-8")
        cipher_suite = Fernet(key)
        byte_enc_token = cipher_suite.decrypt(encrypted_token)
        enc_token = byte_enc_token.decode("utf-8")
        return enc_token
    else:
        enc_token = write_enc_secret(file_name)
        return enc_token


def write_enc_secret(file_name):
    """Converts a string to bytes, generates an encryption key, encrypts the token,
    and stores encrypted key and secret in a list"""
    file_path = pathlib.Path.home() / (file_name + ".enc")
    enc_token = getpass.getpass("Enter your secret:")
    byte_enc_token = bytes(enc_token, "utf-8")
    """
    Convert string to bytes
    """
    key = Fernet.generate_key()
    """
    Generate an encryption key
    """
    cipher_suite = Fernet(key)
    encrypted_token = cipher_suite.encrypt(byte_enc_token)
    """
    Encrypt the token
    """
    enc_pair = key.decode("utf-8") + "," + encrypted_token.decode("utf-8")
    """
    Store encrypted key and secret in a list
    """
    with open(file_path, "w") as enc_file:
        enc_file.write(enc_pair)
    return enc_token

def main():
    parser = argparse.ArgumentParser(description="Handle encrypted secrets.")
    parser.add_argument("file_name", help="Name of the file to store/retrieve the encrypted secret")
    args = parser.parse_args()

    secret = get_enc_secret(args.file_name)
    print("Your secret is:", secret)

if __name__ == "__main__":
    main()