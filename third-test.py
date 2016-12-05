import unittest
import third

class Test_third(unittest.TestCase):

    def test_if_string(self):
        self.assertEqual(third.count_letter_in_string("lobab", "b"), 3)

    def test_if_empty_string(self):
        self.assertEqual(third.count_letter_in_string("", "b"), 0)

    def test_if_empty_letter_string(self):
        self.assertEqual(third.count_letter_in_string("", ""), 0)

    def test_if_uppercase(self):
        self.assertNotEqual(third.count_letter_in_string("JohnnyFirpo", "n"), 4)

    def test_if_list(self):
        self.assertEqual(third.count_letter_in_string([3,5,7,9,8], "8"), 0)

    def test_count_if_boolean(self):
        self.assertEqual(third.count_letter_in_string(True, "b"), 0)

if __name__ == '__main__':
    unittest.main()
