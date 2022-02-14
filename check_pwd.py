def check_pwd(password):
    value = True
    value2 = True

    if len(password) > 8 or len(password) > 20:
        return False

    for j in password:
        value = False
        value2 = False

        if j.islower():
            value = True

        if j.isupper():
            value2 = True

        if value and value2:
            return True
        else:
            return False
    
    if not value:
        return False

