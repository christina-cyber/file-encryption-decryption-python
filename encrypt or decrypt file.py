from cryptography.fernet import Fernet
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Run this once to generate and save a key
generate_key()
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)

    print(f"File {file_path} encrypted successfully.")
def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)

    print(f"File {file_path} decrypted successfully.")
encrypt_file("secret.txt")
decrypt_file("secret.txt")

