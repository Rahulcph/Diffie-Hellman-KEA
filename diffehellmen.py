# Import the secrets module for generating secure random numbers
import secrets

# A prime number (p) and a primitive root modulo p (g)
p = 41 # Prime number
g = 5   # Primitive root modulo p

# Each party selects a private key (random number)
private_key_A = secrets.randbelow(p)  # Private key of party A
private_key_B = secrets.randbelow(p)  # Private key of party B

# Each party computes their public key
public_key_A = pow(g, private_key_A, p)  # Public key of party A
public_key_B = pow(g, private_key_B, p)  # Public key of party B

# Each party computes the shared secret key using the other party's public key
shared_secret_A = pow(public_key_B, private_key_A, p)  # Shared secret for party A
shared_secret_B = pow(public_key_A, private_key_B, p)  # Shared secret for party B

# Both shared secrets should be identical
assert shared_secret_A == shared_secret_B

print(f"Prime (p): {p}")
print(f"Generator (g): {g}")
print(f"Private Key A: {private_key_A}")
print(f"Private Key B: {private_key_B}")
print(f"Public Key A: {public_key_A}")
print(f"Public Key B: {public_key_B}")
print(f"Shared Secret: {shared_secret_A}")
