'''
Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria 
(i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  
Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.'''

class InvalidPasswordError(Exception):
    """InvalidPassword"""


def validate_password(password:str) -> None:
    
    u = 0
    j = 0
    for i in password:
        if not i.isupper():
            u += 1
        if not i.isalnum():
            j += 1

    if len(password) > 20 and u >= 3 and j >= 4:
        print("Valid!")
    else:
        raise InvalidPasswordError(f"The password {password} is weak!!! CHANGE IT NOW!!!")
    

validate_password("Ciao")