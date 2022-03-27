"""
Keyword arguments:
argument -- description
Return: return_description
"""


def username_helper(username):
    try:
        if username is not None:
            return username
        else:
            return "username not found"
    except Exception as ex:
        return str(ex)

def email_helper(email):
    try:
        if email is not None:
            return email
        else:
            return "email not found"
    except Exception as ex:
        return str(ex)

def password_helper(password):
    if password is not None:
        return password
    else:
        return "Invalid password"

