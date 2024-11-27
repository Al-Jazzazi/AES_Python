from Crypto.Cipher import AES
import os
import argparse


def generate_key():
    """Generate a random AES key."""
    return os.urandom(16)


def encrypt_file(file_data, key):
    """Encrypt the file data using AES in EAX mode."""
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(file_data)
    return ciphertext, cipher.nonce, tag


def decrypt_data(ciphertext, key, nonce, tag):
    """Decrypt the ciphertext and verify authenticity."""
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)


def main():
    parser = argparse.ArgumentParser(description="Encrypt and decrypt a file.")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()

    key = generate_key()

    with open(args.filename, "rb") as file:
        data = file.read()

    ciphertext, nonce, tag = encrypt_file(data, key)
    print(f"Ciphertext: {ciphertext}")

    try:
        decrypted_data = decrypt_data(ciphertext, key, nonce, tag)
        decrypted_data = decrypted_data.decode('utf-8')
        print("The message is authentic:", decrypted_data)
    except ValueError:
        print("Key incorrect or message corrupted")


if __name__ == "__main__":
    main()
