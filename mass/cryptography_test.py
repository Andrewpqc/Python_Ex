from cryptography.fernet import Fernet
key = Fernet.generate_key()
print("key:",key)
f = Fernet(key)
token = f.encrypt("this is a test key string".encode())
print("token:",token.decode())

origin = f.decrypt(token)
print("origin:",origin)
