# # app/utils/encryption.py
# from cryptography.fernet import Fernet
# import os

# SECRET_KEY = os.getenv("SECRET_KEY")
# fernet = Fernet(SECRET_KEY.encode())

# def encrypt_token(token: str) -> str:
#     return fernet.encrypt(token.encode()).decode()

# def decrypt_token(token: str) -> str:
#     return fernet.decrypt(token.encode()).decode()
