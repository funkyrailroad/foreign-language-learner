from django.test import TestCase, TransactionTestCase
from django.core.files.uploadedfile import SimpleUploadedFile


import fll.util as u


class TranscriptionTests(TestCase):
    def setUp(self):
        self.fp = "./fll/Voice 182.wav"
        self.gt_text = "Things to do whenever I'm in a new place. Find a pull-up bar."

    def test_send_file_in_request(self):
        resp = self.client.post(
            "/fll/transcribe/",
            data={
                "audio": open(self.fp, "rb"),
            },
        )
        data = resp.json()
        transcription = data["transcription"]
        self.assertEqual(transcription, self.gt_text)

    def test_transcribe_audio(self):
        transcription = u.transcribe_audio_with_whisper(self.fp)
        self.assertEqual(transcription, self.gt_text)

    def test_audio_input(self):
        pass


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


class AudioNoteHyperlinkedViewSetTests(TransactionTestCase):
    def setUp(self):
        super().setUp()
        self.fp = "./fll/Voice 182.wav"
        self.english = "I want to learn foreign languages."
        self.german = "Ich möchte Fremdsprachen lernen."
        self.italian = "Voglio imparare le lingue straniere."
        self.spanish = "Quiero aprender idiomas extranjeros."
        self.swahili = "Nataka kujifunza lugha za kigeni."

    def test_create(self):
        resp = self.client.post(
            "/fll/audio-notes/?serializer=hyperlinked",
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
        url = data["url"] + "?serializer=hyperlinked"

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["english"], self.english)
        self.assertEqual(data["german"], self.german)
        self.assertEqual(data["italian"], self.italian)
        self.assertEqual(data["spanish"], self.spanish)
        self.assertEqual(data["swahili"], self.swahili)


class AudioNoteCustomViewSetTests(TransactionTestCase):
    def setUp(self):
        super().setUp()
        self.fp = "./fll/Voice 182.wav"
        self.english = "Things to do whenever I'm in a new place. Find a pull-up bar."
        self.german = "Dinge, die ich tun kann, wenn ich an einem neuen Ort bin. Finde eine Klimmzugstange."
        self.italian = "Cose da fare ogni volta che mi trovo in un posto nuovo. Trova una barra per trazioni."
        self.spanish = "Cosas que hacer cuando estoy en un lugar nuevo. Busca una barra de dominadas."
        self.swahili = "Mambo ya kufanya wakati wowote ninapokuwa katika nafasi mpya. Pata bar ya kuvuta."

    def test_create(self):
        serializer_qp = "?serializer=custom"

        audio = SimpleUploadedFile(self.fp, b"dummy_fn", content_type="audio/wav")

        headers = {
            'Content-Disposition': 'attachment; filename=my_file.txt'
        }
        resp = self.client.post(
            "/fll/audio-notes/" + serializer_qp,
            data={
                "audio_hash": open(self.fp, "rb"),
                # "audio_hash": audio,
                # "name": "dummy_fn.wav",
            },
            headers=headers,
        )
        self.assertEqual(resp.status_code, 201, resp.json())
        data = resp.json()
        self.assertEqual(data["german"], self.german)
        self.assertEqual(data["italian"], self.italian)
        self.assertEqual(data["spanish"], self.spanish)
        self.assertEqual(data["swahili"], self.swahili)
        self.assertEqual(data["english"], self.english)
        breakpoint()
