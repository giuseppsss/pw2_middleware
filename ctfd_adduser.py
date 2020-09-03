import secrets
import string

def get_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(10)) # for a 10-character password
    print(password)
    return(password)

def get_adduser():
    print("ciao")
