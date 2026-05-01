import unittest

def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

class TestPalindromeFunction(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("Hello, World!"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_non_alphanumeric_characters(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

if __name__ == '__main__':
    unittest.main()
