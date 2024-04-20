import os
from django.test import TestCase

import fll.util as u

class TranscriptionTests(TestCase):
    def test_transcribe_audio(self):
        fp = "./fll/Voice 182.wav"
        with open(fp) as f:
            print(f)
        transcription = u.transcribe_audio_with_whisper(fp)
        gt_text = "Things to do whenever I'm in a new place. Find a pull-up bar."
        self.assertEqual(transcription, gt_text)


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


class AudioNoteViewSetTests(TestCase):
    def setUp(self):
        super().setUp()
        self.english = "I want to learn foreign languages."
        self.german = "Ich möchte Fremdsprachen lernen."
        self.italian = "Voglio imparare le lingue straniere."
        self.spanish = "Quiero aprender idiomas extranjeros."
        self.swahili = "Nataka kujifunza lugha za kigeni."

    def test_create(self):
        resp = self.client.post(
            "/fll/audio-notes/",
            data={
                "english": self.english,
                "german": self.german,
                "italian": self.italian,
                "spanish": self.spanish,
                "swahili": self.swahili,
            },
        )
        self.assertEqual(resp.status_code, 201)
        data = resp.json()
        url = data["url"]

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["english"], self.english)
        self.assertEqual(data["german"], self.german)
        self.assertEqual(data["italian"], self.italian)
        self.assertEqual(data["spanish"], self.spanish)
        self.assertEqual(data["swahili"], self.swahili)
