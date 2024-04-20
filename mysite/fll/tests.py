from django.test import TestCase

import fll.util as u


class TranslationTests(TestCase):
    def setUp(self):
        super().setUp()
        self.text = "I want to learn foreign languages."

    def test_translate_to_german(self):
        gt_translation = "Ich möchte Fremdsprachen lernen."

        translation = u.translate_to_german(self.text)
        self.assertEqual(translation, gt_translation)

    def test_translate_to_italian(self):
        gt_translation = "Voglio imparare le lingue straniere."

        translation = u.translate_to_italian(self.text)
        self.assertEqual(translation, gt_translation)

    def test_translate_to_spanish(self):
        gt_translation = "Quiero aprender idiomas extranjeros."

        translation = u.translate_to_spanish(self.text)
        self.assertEqual(translation, gt_translation)

    def test_translate_to_swahili(self):
        gt_translation = "Nataka kujifunza lugha za kigeni."

        translation = u.translate_to_swahili(self.text)
        self.assertEqual(translation, gt_translation)
