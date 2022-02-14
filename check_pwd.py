def check_pwd(password):
    lowercase_check = 0
    uppercase_check = 0
    symbol_check = 0
    number_check = 0

    # array of symbols characters, to make it easier to check if present in pwd
    symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*',
               '(', ')', '_', '+', '-', '=']

    if len(password) > 8 or len(password) > 20:
        return False

    # since it only needs at LEAST one, and not exactly one, I can let if return True if anything other than 0
    # https://www.w3schools.com/python/ref_string_isdigit.asp
    # referenced this to learn about .isdigit() method
    for j in password:
        if j.islower():
            lowercase_check = 1
        elif j.isupper():
            uppercase_check = 1
        elif j in symbols:
            symbol_check = 1
        elif j.isdigit():
            number_check = 0

    # https://stackoverflow.com/questions/20002503/why-does-a-x-or-y-or-z-always-evaluate-to-true
    # referenced this to condense ugly list of code
    if {lowercase_check, uppercase_check, symbol_check, number_check} == 0:
        return False

    else:
        return True
