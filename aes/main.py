import aes

key = b'master key'
message = b'secret message from Mark Yavorskyi'

encrypted_message = aes.encrypt(key, message)
print(encrypted_message)
print(aes.decrypt(key, encrypted_message))