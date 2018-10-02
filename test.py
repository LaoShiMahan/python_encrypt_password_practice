import bcrypt

def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password.encode("utf8"), bcrypt.gensalt())

print(get_hashed_password("verysecurepassword"))

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode("utf8"), hashed_password.encode("utf8"))

print(check_password("verysecurepassword", "$2b$12$9QpWvXSvagNrRCu/OZ99A.ynRRA6rymAlohxZc1j/pck/Ea2OI1rW"))