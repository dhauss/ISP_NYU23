import hashlib

hash1234 = hashlib.sha256(b'1234')
print(len(hash1234.hexdigest()))
