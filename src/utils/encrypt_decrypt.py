from cryptography.fernet import Fernet


def encrypt(secret_key: str, text: str):
    fernet = Fernet(secret_key)
    return fernet.encrypt(text.encode()).decode()


def decrypt(secret_key: str, text: str):
    fernet = Fernet(secret_key)
    return fernet.decrypt(text.encode()).decode()
