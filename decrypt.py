from cryptography.fernet import Fernet, InvalidToken
import sys

def generate_key_from_number(number):
    """ Generate a key based on a number. """
    return Fernet.generate_key() + str(number).encode()

def decrypt_file(encrypted_file_path, key_number):
    """ Decrypt the contents of the encrypted file using the key. """
    # Generate key
    key = generate_key_from_number(key_number)
    cipher_suite = Fernet(key)

    # Read the encrypted data
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt data
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data)
    except InvalidToken:
        print("Invalid key or corrupted data.")
        return

    # Print the decrypted data
    print("Decrypted data:")
    print(decrypted_data.decode())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decrypt.py [path_to_encrypted_file] [key_number]")
    else:
        file_path = sys.argv[1]
        key_number = int(sys.argv[2])
        if 1000 <= key_number <= 5000:
            decrypt_file(file_path, key_number)
        else:
            print("Key number must be between 1000 and 5000.")
