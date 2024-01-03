import secrets

def generate_secret_key(length=32):


    return secrets.token_hex(length//2)

secret_key = generate_secret_key()

print('Generated SECRET_KEY:', secret_key)