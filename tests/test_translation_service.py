import unittest
from src.translation_service import translate_to_french

class TestTranslationService(unittest.TestCase):
    def test_valid_translation(self):
        self.assertEqual(translate_to_french("Hello"), "Bonjour")
        self.assertEqual(translate_to_french("Goodbye"), "Au revoir")

    def test_empty_string(self):
        self.assertEqual(translate_to_french(""), "")

    def test_unsupported_characters(self):
        self.assertEqual(translate_to_french("12345"), "12345")

    def test_special_characters(self):
        self.assertEqual(translate_to_french("Café"), "Café")

if __name__ == '__main__':
    unittest.main()
