import sys
from cryptography.fernet import Fernet

def file_decryption(source_file, target_file, key):
    with open(source_file, 'rb') as file:
        encrypted_content = file.read()

    fernet = Fernet(key)
    decrypted_content = fernet.decrypt(encrypted_content)

    with open(target_file, 'wb') as file:
        file.write(decrypted_content)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python decrypt.py <source_file> <target_file> <key>")
        sys.exit(1)

    source_file = sys.argv[1]
    target_file = sys.argv[2]
    key = sys.argv[3].encode()

    file_decryption(source_file, target_file, key)
    print("File decrypted successfully.")
