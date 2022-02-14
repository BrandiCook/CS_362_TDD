# Brandi Cook
# 93309286
# TDD Hands On, A2, Due 2/14/2022

import unittest
from unittest import TestCase
from check_pwd import check_pwd


# Class definition

# Must be between 8 and 20 characters (inclusive)
# Must contain at least one lowercase letter
# Must contain at least one uppercase letter
# Must contain at least one digit
# Must contain at least one symbol from: ~`!@#$%^&*()_+-=
# (copy and paste to avoid missing characters) These are the only permitted symbols

class Test_Password_Validator(TestCase):
    def test_empty(self):
        password = ""
        self.assertFalse(check_pwd(password))

    def test_len_7(self):
        password = "abcdefg"
        self.assertFalse(check_pwd(password))

    def test_len_21(self):
        password = "abcdefghijklmnopqrstu"
        self.assertFalse(check_pwd(password))

    def test_uppercase(self):
        password = "ABCDEFGH"
        self.assertTrue(check_pwd(password))

    def test_lowercase(self):
        password = "abcdefgh"
        self.assertTrue(check_pwd(password))

    def test_symbols(self):
        password = "~`!@#$%^&*()_+-="  # 16 chars
        self.assertTrue(check_pwd(password))


if __name__ == '__main__':
    unittest.main()
