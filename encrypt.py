from cryptography.fernet import Fernet
import sys

def generate_key_from_number(number):
    """ Generate a key based on a number. """
    return Fernet.generate_key() + str(number).encode()

def encrypt_file(file_path, key_number):
    """ Encrypt the contents of the file using the key. """
    # Generate key
    key = generate_key_from_number(key_number)
    cipher_suite = Fernet(key)

    # Read the contents of the file
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt data
    encrypted_data = cipher_suite.encrypt(file_data)

    # Write the encrypted data to a new file
    with open(file_path + ".encrypted", 'wb') as file:
        file.write(encrypted_data)

    print("File encrypted successfully.")

if __name__ == "__main__":
    key_number = 1500
    encrypt_file("message.txt", key_number)
