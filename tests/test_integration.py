import unittest
from src.components.language_selector import LanguageSelector
from src.translation_service import translate_to_french

class TestIntegration(unittest.TestCase):
    def test_language_selection_triggers_translation(self):
        selector = LanguageSelector()
        selector.select_language("French")
        translated_text = translate_to_french("Hello")
        self.assertEqual(translated_text, "Bonjour")

if __name__ == '__main__':
    unittest.main()
