import unittest
import random
import cipher


class CaesarCipherTest(unittest.TestCase):
    # Default tests
    def test_encode_default(self):
        self.assertEqual(cipher.encrypt(cipher.TEST_STR, cipher.TEST_KEY), cipher.TEST_CIP)
    def test_decode_default(self):
        self.assertEqual(cipher.decrypt(cipher.TEST_CIP, cipher.TEST_KEY), cipher.TEST_STR)
    def test_encode_decode_default(self):
        self.assertEqual(cipher.decrypt(cipher.encrypt("test_encode_decode_default  ", 8)), "TESTENCODEDECODEDEFAULT")
        self.assertEqual(cipher.decrypt(cipher.encrypt("test_encode_decode_default  ", 25)), "TESTENCODEDECODEDEFAULT")
        self.assertEqual(cipher.decrypt(cipher.encrypt("test_encode_decode_default  ", 0)), "TESTENCODEDECODEDEFAULT")
    
    # Key tests
    def test_key_zero(self):
        self.assertEqual(cipher.encrypt("test if key is zero"), "TESTIFKEYISZERO")
        self.assertEqual(cipher.encrypt("test_if_key_is_zero", 0), "TESTIFKEYISZERO")
    def test_key_edge_cases(self):
        self.assertEqual(cipher.encrypt("test if key is zero", 0), "TESTIFKEYISZERO")
        self.assertEqual(cipher.decrypt("test if key is zero", 0), "TESTIFKEYISZERO")
        self.assertEqual(cipher.encrypt("test if key is twenty-six", 26), "TESTIFKEYISTWENTYSIX")
        self.assertEqual(cipher.decrypt("test if key is twenty-six", 26), "TESTIFKEYISTWENTYSIX")
    def test_large_key(self):
        self.assertEqual(cipher.encrypt("Test if large key", 100), "paopebhwncagau".upper())
        self.assertEqual(cipher.encrypt("Test if large key", 12345), "oznodagvmbzfzt".upper())
        self.assertEqual(cipher.decrypt("paopebhwncagau", 100), "TESTIFLARGEKEY")
        self.assertEqual(cipher.decrypt("alzapmshynlrlf", 54321), "TESTIFLARGEKEY")
    def test_negative_key(self):
        self.assertEqual(cipher.encrypt("test if negative key", -5), cipher.encrypt("test if negative key", 21))
        self.assertEqual(cipher.encrypt("test if negative key", -17), cipher.encrypt("test if negative key", 9))
        self.assertEqual(cipher.decrypt("kvjkzwevxrkzmvbvp", -9), cipher.decrypt("kvjkzwevxrkzmvbvp", 17))
        self.assertEqual(cipher.decrypt("zkyzoltkmgzobkqke", -20), cipher.decrypt("zkyzoltkmgzobkqke", 6))
    def test_random_key(self):
        random.seed()
        r = random.randrange(0, 26)
        self.assertEqual(cipher.decrypt(cipher.encrypt("Test random key", r), r), "TESTRANDOMKEY")

    # String content tests
    def test_empty_string(self):
        self.assertEqual(cipher.encrypt(""), cipher.EMPTY_STRING_MSG)
        self.assertEqual(cipher.decrypt(""), cipher.EMPTY_STRING_MSG)
        self.assertEqual(cipher.encrypt("                 "), cipher.EMPTY_STRING_MSG)
        self.assertEqual(cipher.decrypt("                 "), cipher.EMPTY_STRING_MSG)
    def test_no_letters_in_string(self):
        self.assertEqual(cipher.encrypt("[]12~!*7^&", 23), cipher.EMPTY_STRING_MSG)
        self.assertEqual(cipher.decrypt("=!@#!~$+?", 24), cipher.EMPTY_STRING_MSG)
        self.assertEqual(cipher.encrypt("*{;|&$@#138953#*(", 25), cipher.EMPTY_STRING_MSG)
        self.assertEqual(cipher.decrypt("?.>-83{67@3\!;`2=", 26), cipher.EMPTY_STRING_MSG)
    def test_digits_in_string(self):
        self.assertEqual(cipher.encrypt("the password is 1234", 15), "iwtephhldgsxh".upper())
        self.assertEqual(cipher.encrypt("1234567890", 12), cipher.EMPTY_STRING_MSG)
        self.assertEqual(cipher.encrypt("testif000digits23in1string", 15), "cnbcromrprcbrwbcarwp".upper())


if __name__ == '__main__':
    unittest.main()
