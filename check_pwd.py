def check_pwd(password):
    value = True

    if len(password) > 8 or len(password) > 20:
        return False

    for j in password:
        value = False
        if j.islower():
            value = True
        if j.isupper():
            value = True
        return value
    if not value:
        return False

