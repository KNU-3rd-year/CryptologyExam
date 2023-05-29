import hashlib
import random
from sympy import isprime


def generate_prime(bit_length):
    while True:
        p = random.getrandbits(bit_length)
        if isprime(p):
            return p


def modular_inverse(a, m):
    if a < 0:
        a = m + (a % m)
    _, x, _ = extended_gcd(a, m)
    return x % m


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def generate_keys():
    q = generate_prime(256)
    p = 2 * q + 1
    while not isprime(p):
        q = generate_prime(256)
        p = 2 * q + 1

    g = random.randint(2, p - 1)

    x = random.randint(2, q - 1)
    y = pow(g, x, p)

    return (p, q, g, y, x)


def sign(message, private_key):
    p, q, g, y, x = private_key

    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    k = random.randint(2, q - 1)
    r = pow(g, k, p) % q

    s = (modular_inverse(k, q) * (h + x * r)) % q

    return (r, s)


def verify(message, signature, public_key):
    p, q, g, y = public_key
    r, s = signature

    if r < 1 or r > q - 1 or s < 1 or s > q - 1:
        return False

    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    w = modular_inverse(s, q)
    u1 = (h * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p)) % p % q

    return v == r


message = "Hello, world!"
private_key = generate_keys()
public_key = private_key[:-1]
signature = sign(message, private_key)

print("Message:", message)
print("Public Key:", public_key)
print("Signature:", signature)
print("Verification:", verify(message, signature, public_key))
