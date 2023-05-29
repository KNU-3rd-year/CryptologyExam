import aes

key = b'master key'
message = b'secret message from Mark Yavorskyi'

ciphertext = aes.encrypt(key, message)
print(ciphertext)
print(aes.decrypt(key, ciphertext))