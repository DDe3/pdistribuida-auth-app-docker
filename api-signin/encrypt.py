from passlib.hash import sha256_crypt


def encrypt_password(password):
    e_password = sha256_crypt.encrypt(password)
    return e_password

def verify_password(password, e_password):
    return sha256_crypt.verify(password, e_password)
