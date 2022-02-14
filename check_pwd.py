def check_pwd(password):
    if len(password) > 7 or len(password) < 21:
        return False
    else:
        return True
