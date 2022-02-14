def check_pwd(password):
    lowercase_check = 0
    uppercase_check = 0

    if len(password) > 8 or len(password) > 20:
        return False

    for j in password:
        if j.islower():
            lowercase_check = 1
        elif j.isupper():
            uppercase_check = 1

    if lowercase_check == 0 or uppercase_check == 0:
        return False

    else:
        return True
