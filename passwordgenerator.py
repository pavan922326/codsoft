import time
import secrets
import string

def generate_custom_password(length=5,
                             use_upper=True,
                             use_lower=False,
                             use_digits=False):
    alphabet = ''
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_lower:
        alphabet += string.ascii_lowercase
    if use_digits:
        alphabet += string.digits
    if not alphabet:
        raise ValueError("Choose at least one character type")
    return ''.join(secrets.choice(alphabet) for _ in range(length))
print(generate_custom_password(5, use_upper=False, use_lower=True, use_digits=True))
time.sleep(2)
print("END OF AN APPLICATION")

