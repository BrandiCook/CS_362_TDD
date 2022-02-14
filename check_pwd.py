def check_pwd(password):
    if len(password) < 7 or len(password) > 20:
        return False
    else:
        return True
