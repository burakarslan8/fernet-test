import sys
from cryptography.fernet import Fernet

def file_encryption(source_file, target_file, key):
    with open(source_file, 'rb') as file:
        content = file.read()

    fernet = Fernet(key)
    encrypted_content = fernet.encrypt(content)

    with open(target_file, 'wb') as file:
        file.write(encrypted_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <source_file> <target_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    target_file = sys.argv[2]
    key = Fernet.generate_key()

    file_encryption(source_file, target_file, key)
    print("File encrypted successfully. Key:", key.decode())
