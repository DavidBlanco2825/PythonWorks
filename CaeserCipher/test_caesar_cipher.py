import unittest
from caesar_cipher import caesar


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(caesar("", 5, "encode"), "")
        self.assertEqual(caesar("abc", 0, "encode"),"abc")
        self.assertEqual(caesar("abc", 1, "encode"), "bcd")
        self.assertEqual(caesar("abc", 5, "encode"), "fgh")
        self.assertEqual(caesar("abc", 35, "encode"), "jkl")
        self.assertEqual(caesar("hello, world!", 15, "encode"), "wtaad, ldgas!")

    def test_decrypt(self):
        self.assertEqual(caesar("", 5, "decode"), "")
        self.assertEqual(caesar("abc", 0, "decode"), "abc")
        self.assertEqual(caesar("bcd", 1, "decode"), "abc")
        self.assertEqual(caesar("fgh", 5, "decode"), "abc")
        self.assertEqual(caesar("jkl", 35, "decode"), "abc")
        self.assertEqual(caesar("wtaad, ldgas!", 15, "decode"), "hello, world!")