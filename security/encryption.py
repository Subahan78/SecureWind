from cryptography.fernet import Fernet


# Create a new encryption key
def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("Encryption key generated successfully!")


# Load the saved key
def load_key():
    return open("secret.key", "rb").read()


# Encrypt a file
def encrypt_file(filename):

    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"{filename} encrypted successfully!")


# Decrypt a file
def decrypt_file(filename):

    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filename, "wb") as dec_file:
        dec_file.write(decrypted)

    print(f"{filename} decrypted successfully!")