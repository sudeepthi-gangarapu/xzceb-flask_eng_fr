import unittest

from translator import french_to_english, english_to_french

class TestfrenchToEnglish(unittest.TestCase):

    def test1(self):

        self.assertEqual(french_to_english(""),"")

        self.assertEqual(french_to_english("Bonjour"),"Hello")



class TestenglishToFrench(unittest.TestCase):

    def test1(self):

        self.assertEqual(english_to_french(""),"")

        self.assertEqual(english_to_french("Hello"),"Bonjour")



unittest.main()