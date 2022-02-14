def check_pwd(password):

    if len(password) > 8 or len(password) > 20:
        return False

    for j in password:
        value = False
        value2 = False

        if j.islower():
            value = True

        if j.isupper():
            value2 = True

        if not value and not value2:
            return False

        else:
            return False

    else:
        return False

