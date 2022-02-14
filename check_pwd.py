def check_pwd(password):
    lowercase_check = 0
    uppercase_check = 0
    symbol_check = 0

    # array of symbols characters, to make it easier to check if present in pwd
    symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*',
               '(', ')', '_', '+', '-', '=']

    if len(password) > 8 or len(password) > 20:
        return False

    # since it only needs at LEAST one, and not exactly one, I can let if return True if anything other than 0
    for j in password:
        if j.islower():
            lowercase_check = 1
        elif j.isupper():
            uppercase_check = 1
        elif j in symbols:
            symbol_check = 1

    # this is ugly but it works
    if lowercase_check == 0 or uppercase_check == 0 or symbol_check == 0:
        return False

    else:
        return True
